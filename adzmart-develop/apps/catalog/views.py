from django import forms
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.urls import reverse_lazy, reverse
from django.core.mail import EmailMessage
from django.template.loader import get_template
from cloudinary.forms import cl_init_js_callbacks
import cloudinary
import json
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
import logging
from django.shortcuts import get_object_or_404


from apps.catalog.utilities import DivErrorList
from apps.catalog.models import (
    Unit,
    UnitType,
    RadioUnit,
    TVUnit,
    BillboardImage,
    CinemaUnit,
    SpecialOffers,
    PrintUnit
)
from .forms import (
    UnitForm,
    ExcelUploadForm,
    AddStaffForm,
    RadioUnitForm,
    TVUnitForm,
    BillboardImageForm,
    CinemaUnitForm,
    CinemaUnitExcelUploadForm,
    SpecialOffersForm,
    PrintUnitForm,
    PrintUnitExcelUploadForm,
)
from apps.authentication.models import Supplier, User, Invitation
from apps.authentication.utilities import EmailThread

log = logging.getLogger(__name__)


def index(request):
    if request.user.is_authenticated:
        user = get_object_or_404(User, email=request.user.email)
        supplier = user.supplier
        context = {}
        users = User.objects.filter(supplier=supplier)
        context["supplier"] = supplier
        context["billboard_count"] = Unit.objects.filter(user=supplier.owner).count()
        context["radio_count"] = RadioUnit.objects.filter(user=supplier.owner).count()
        context["tv_count"] = TVUnit.objects.filter(user=supplier.owner).count()
        context["total_users"] = users.count()
        if not context["supplier"].is_verified:
            messages.info(
                request,
                message="Your account is undergoing our verification process.\
                                            You'll be notified once your account has been verified.",
            )
        return render(request, "catalog/dashboard.html", context)
    return render(request, "catalog/dashboard.html")


def load_billboard_catalog(request):
    user = get_object_or_404(User, email=request.user.email)
    supplier = user.supplier.owner
    context = {}
    context["supplier"] = Supplier.objects.filter(owner=supplier).first()
    context["catalog"] = Unit.objects.filter(user=supplier)
    return render(request, "catalog/billboard/billboard_inventory.html", context)


def load_radio_catalog(request):
    user = get_object_or_404(User, email=request.user.email)
    supplier = user.supplier.owner
    context = {}
    context["supplier"] = Supplier.objects.filter(owner=supplier).first()
    context["catalog"] = RadioUnit.objects.filter(user=supplier)
    return render(request, "catalog/radio/inventory.html", context)


def load_tv_catalog(request):
    user = get_object_or_404(User, email=request.user.email)
    supplier = user.supplier.owner
    context = {}
    context["supplier"] = Supplier.objects.filter(owner=supplier).first()
    context["catalog"] = TVUnit.objects.filter(user=supplier)
    return render(request, "catalog/tv/inventory.html", context)


def upload_billboard_catalog(request, **kwargs):
    if request.method == "POST":
        form = ExcelUploadForm(request.POST, request.FILES, error_class=DivErrorList)
        if form.is_valid():
            unit_obj = form.save(request, form, **kwargs)
            if unit_obj:
                return redirect("catalog:upload_excel_billboard_image")
    else:
        form = ExcelUploadForm()
    return render(
        request,
        "catalog/common/importexcel.html",
        {
            "form": form,
            "inventory": "billboard",
            "action": reverse_lazy(kwargs["action"]),
        },
    )


def add_billboard_unit(request):
    if request.method == "POST":
        form = UnitForm(request.POST, error_class=DivErrorList)
        if form.is_valid():
            unit = form.save(commit=False)
            unit.user = request.user.supplier.owner
            unit.country = request.POST["country"]
            unit.state = request.POST["state"]
            unit.save()
            messages.success(
                request,
                message="Unit added successfully. You can now upload billboard images.",
            )
            return redirect("catalog:upload_form_billboard_image", id=unit.id)

    else:
        form = UnitForm()
    return render(request, "catalog/billboard/add_billboard_unit.html", {"form": form})


def upload_form_billboard_image(request, id):
    """
    Handles billboard image upload from forms.
    """
    direct_form = BillboardImageForm()
    billboard_unit = get_object_or_404(Unit, id=id)
    context = dict(direct_form=direct_form, unit=billboard_unit)
    cl_init_js_callbacks(context["direct_form"], request)
    context["posted"] = direct_form.instance

    if request.method == "POST":
        form = BillboardImageForm(request.POST)
        if form.is_valid():
            unit_image = form.save(commit=False)
            unit_image.image_public_id = form.instance.image
            unit_image.reference_id = billboard_unit.reference_id
            unit_image.save()
    return render(
        request, "catalog/billboard/upload-form-billboard-image.html", context
    )


def upload_excel_billboard_image(request):
    """
    Handles billboard image upload for excel.
    """
    direct_form = BillboardImageForm()
    context = dict(direct_form=direct_form)
    cl_init_js_callbacks(context["direct_form"], request)
    context["posted"] = direct_form.instance

    if request.method == "POST":
        form = BillboardImageForm(request.POST)
        if form.is_valid():
            unit_image = form.save(commit=False)
            unit_image.image_public_id = form.instance.image
            unit_image.save()
    return render(
        request, "catalog/billboard/upload-excel-billboard-image.html", context
    )


def update_excel_billboard_image(request):
    """
    Makes AJAX Request to update instances of billboard images
    """
    if request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest":
        file_name = request.GET["response[original_filename]"]
        file_ext = request.GET["response[format]"]
        public_id = request.GET["response[public_id]"]
        uploaded_file_name = f"{file_name}.{file_ext}"
        reference_id = file_name.split("_")[0]
        unit_image_to_update = get_object_or_404(
            BillboardImage, image_public_id=public_id
        )

        try:
            unit_image_to_update.original_filename = uploaded_file_name
            unit_image_to_update.reference_id = reference_id
            unit_image_to_update.save()
        except Exception as e:
            log.error("Error saving billboard images", exc_info=1)

        try:
            billboard_unit_to_update = Unit.objects.get(reference_id=reference_id)
        except ObjectDoesNotExist:
            cloudinary.uploader.destroy(public_id)
            unit_image_to_update.delete()

        return HttpResponse(200)


def edit_billboard_unit(request, pk):
    billboard_unit = Unit.objects.get(id=pk)
    if request.method == "POST":
        form = UnitForm(request.POST, instance=billboard_unit, error_class=DivErrorList)
        if form.is_valid():
            unit = form.save()
            unit.user = request.user.supplier.owner
            unit.country = request.POST["country"]
            unit.state = request.POST["state"]
            unit.save()
            messages.success(request, message="Unit updated successfully!")
            return redirect("catalog:load_billboard_catalog")
    else:
        form = UnitForm(instance=billboard_unit)
    return render(request, "catalog/billboard/billboard_unit_edit.html", {"form": form})


def delete_billboard_unit(request, pk):
    billboard_unit = Unit.objects.get(id=pk)
    if request.method == "POST":
        billboard_unit.delete()
        return redirect("catalog:load_billboard_catalog")
    context = {"billboard_unit": billboard_unit}
    return render(request, "catalog/billboard/billboard_unit_delete.html", context)


def add_radio_unit(request):
    if request.method == "POST":
        form = RadioUnitForm(request.POST, error_class=DivErrorList)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = request.user.supplier.owner
            rate.save()
            messages.success(request, message="Radio Unit added successfully!")
            return redirect("catalog:load_radio_catalog")
    else:
        form = RadioUnitForm()
    return render(request, "catalog/radio/add_radio_unit.html", {"form": form})


def edit_radio_unit(request, pk):
    radio_unit = RadioUnit.objects.get(id=pk)
    if request.method == "POST":
        form = RadioUnitForm(
            request.POST, instance=radio_unit, error_class=DivErrorList
        )
        if form.is_valid():
            unit = form.save()
            unit.user = request.user.supplier.owner
            unit.save()
            messages.success(request, message="Radio Unit updated successfully!")
            return redirect("catalog:load_radio_catalog")
    else:
        form = RadioUnitForm(instance=radio_unit)
    return render(request, "catalog/radio/edit_radio_unit.html", {"form": form})


def delete_radio_unit(request, pk):
    radio_unit = RadioUnit.objects.get(id=pk)
    if request.method == "POST":
        radio_unit.delete()
        return redirect("catalog:load_radio_catalog")
    context = {"radio_unit": radio_unit}
    return render(request, "catalog/radio/delete_radio_unit.html", context)


def upload_radio_catalog(request, **kwargs):
    if request.method == "POST":
        form = ExcelUploadForm(request.POST, request.FILES, error_class=DivErrorList)
        if form.is_valid():
            form.save(request, form, **kwargs)
            return redirect("catalog:load_radio_catalog")
    else:
        form = ExcelUploadForm()
    return render(
        request,
        "catalog/common/importexcel.html",
        {"form": form, "action": reverse_lazy(kwargs["action"])},
    )


def add_tv_unit(request):
    if request.method == "POST":
        form = TVUnitForm(request.POST, error_class=DivErrorList)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = request.user.supplier.owner
            rate.save()
            messages.success(request, message="TV Unit added successfully!")
            return redirect("catalog:load_tv_catalog")
    else:
        form = TVUnitForm()
    return render(request, "catalog/tv/add_tv_unit.html", {"form": form})


def edit_tv_unit(request, pk):
    tv_unit = TVUnit.objects.get(id=pk)
    if request.method == "POST":
        form = TVUnitForm(request.POST, instance=tv_unit, error_class=DivErrorList)
        if form.is_valid():
            unit = form.save()
            unit.user = request.user.supplier.owner
            unit.save()
            messages.success(request, message="TV Unit updated successfully!")
            return redirect("catalog:load_tv_catalog")
    else:
        form = TVUnitForm(instance=tv_unit)
    return render(request, "catalog/tv/edit_tv_unit.html", {"form": form})


def delete_tv_unit(request, pk):
    tv_unit = TVUnit.objects.get(id=pk)
    if request.method == "POST":
        tv_unit.delete()
        return redirect("catalog:load_tv_catalog")
    context = {"tv_unit": tv_unit}
    return render(request, "catalog/tv/delete_tv_unit.html", context)


def upload_tv_catalog(request, **kwargs):
    if request.method == "POST":
        form = ExcelUploadForm(request.POST, request.FILES, error_class=DivErrorList)
        if form.is_valid():
            form.save(request, form, **kwargs)
            return redirect("catalog:load_tv_catalog")
    else:
        form = ExcelUploadForm()
    return render(
        request,
        "catalog/common/importexcel.html",
        {"form": form, "inventory": "tv", "action": reverse_lazy(kwargs["action"])},
    )


def profile(request):
    user = get_object_or_404(User, email=request.user.email)
    supplier = user.supplier
    context = {"supplier": supplier}
    return render(request, "catalog/profile.html", context)


def faqs(request):
    if request.method == "POST":
        data = request.POST
        name = data["name"]
        email = data["email"].lower()
        selected_option = data["subject"]
        message = data["message"]
        # send email notification to admin on submmited ticket
        context = {
            "name": name,
            "email": email,
            "subject": selected_option,
            "message": message,
        }
        message = get_template("submit-ticket.html").render({"context": context})
        subject = "Ticket Submission!"
        try:
            email = EmailMessage(
                subject, message, "noreply@adzmart.com", ["support@adzmart.com"]
            )
            EmailThread(email).start()
            messages.success(
                request,
                "Your ticket has been submitted successfully. We will get back to you soon!",
            )
        except Exception as e:
            messages.error(request, "Error:" + str(e))

    return render(request, "catalog/faqs.html")


def generate_invitation_link(request, user):
    return request.build_absolute_uri(
        reverse(
            "authentication:setup_invite_account",
            kwargs={
                "uidb64": urlsafe_base64_encode(force_bytes(user.pk)),
            },
        )
    )


def staff_users(request):
    user = get_object_or_404(User, email=request.user.email)
    supplier = user.supplier
    users_qs = User.objects.filter(supplier=supplier)
    pending_invites = Invitation.objects.filter(
        supplier=supplier, status__in=["Pending", "Rejected"]
    )
    accepted_invites = Invitation.objects.filter(supplier=supplier, status="Active")
    users = []

    for user in users_qs:
        if supplier.owner != user:
            users.append(
                {
                    "invitation_link": generate_invitation_link(request, user),
                    "is_verified": user.is_verified,
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                }
            )

    context = {
        "users": users,
        "total_users": len(users),
        "total_pending_invites": pending_invites.count(),
        "total_accepted_invites": accepted_invites.count(),
        "supplier": supplier,
    }
    return render(request, "catalog/staffs/staffs.html", context)


def pending_staff_invites(request):
    user = get_object_or_404(User, email=request.user.email)
    supplier = user.supplier
    invites = Invitation.objects.filter(
        supplier=supplier, status__in=["Pending", "Rejected"]
    )
    users = []

    for user in invites:
        users.append(
            {
                "invitation_link": generate_invitation_link(request, user),
                "status": user.status,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
            }
        )
    context = {"invites": users, "supplier": supplier, "total_invites": len(users)}
    return render(request, "catalog/staffs/pending-invites.html", context)


def accepted_staff_invites(request):
    user = get_object_or_404(User, email=request.user.email)
    supplier = user.supplier
    invites = Invitation.objects.filter(supplier=supplier, status="Active")
    context = {"invites": invites, "supplier": supplier, "total_invites": len(invites)}
    return render(request, "catalog/staffs/accepted-invites.html", context)


def load_cinema_catalog(request):
    user = get_object_or_404(User, email=request.user.email)
    supplier = user.supplier.owner
    context = {}
    context["supplier"] = Supplier.objects.filter(owner=supplier).first()
    context["catalog"] = CinemaUnit.objects.filter(user=supplier)
    return render(request, "catalog/cinema/cinema_inventory.html", context)


def add_cinema_unit(request):
    if request.method == "POST":
        form = CinemaUnitForm(request.POST, error_class=DivErrorList)
        if form.is_valid():
            cinema_unit = form.save(commit=False)
            cinema_unit.user = request.user.supplier.owner
            cinema_unit.save()
            messages.success(
                request,
                message="Unit added successfully.",
            )
            return redirect("catalog:load_cinema_catalog")

    else:
        form = CinemaUnitForm()
    return render(request, "catalog/cinema/add_cinema_unit.html", {"form": form})


def edit_cinema_unit(request, pk):
    cinema_unit_obj = get_object_or_404(CinemaUnit, id=pk)
    if request.method == "POST":
        form = CinemaUnitForm(
            request.POST, instance=cinema_unit_obj, error_class=DivErrorList
        )
        if form.is_valid():
            cinema_unit = form.save(commit=False)
            cinema_unit.user = request.user.supplier.owner
            cinema_unit.save()
            messages.success(request, message="Unit updated successfully!")
            return redirect("catalog:load_cinema_catalog")
    else:
        form = CinemaUnitForm(instance=cinema_unit_obj)
    return render(request, "catalog/cinema/cinema_unit_edit.html", {"form": form})


def delete_cinema_unit(request, pk):
    cinema_unit = get_object_or_404(CinemaUnit, id=pk)
    if request.method == "POST":
        cinema_unit.delete()
        return redirect("catalog:load_cinema_catalog")
    context = {"cinema_unit": cinema_unit}
    return render(request, "catalog/cinema/cinema_unit_delete.html", context)


def upload_cinema_catalog(request, **kwargs):
    if request.method == "POST":
        form = CinemaUnitExcelUploadForm(
            request.POST, request.FILES, error_class=DivErrorList
        )
        if form.is_valid():
            form.save(request, form, **kwargs)
            return redirect("catalog:load_cinema_catalog")
    else:
        form = CinemaUnitExcelUploadForm
    return render(
        request,
        "catalog/common/importexcel.html",
        {
            "form": form,
            "inventory": "cinema",
            "action": reverse_lazy(kwargs["action"]),
        },
    )


def load_special_offers(request):
    user = get_object_or_404(User, email=request.user.email)
    supplier = user.supplier.owner
    context = {}
    context["supplier"] = Supplier.objects.filter(owner=supplier).first()
    context["catalog"] = SpecialOffers.objects.filter(user=supplier)
    return render(request, "catalog/special-offers/special_offers_inventory.html", context)


def add_special_offer(request):  
    if request.method == "POST":
        form = SpecialOffersForm(request.POST, request.FILES, error_class=DivErrorList)
        if form.is_valid():
            special_offer = form.save(commit=False)
            special_offer.user = request.user.supplier.owner
            special_offer.save()
            messages.success(
                request,
                message="Your special offer has been created successfully.",
            )
            return redirect("catalog:load_special_offers")

    else:
        form = SpecialOffersForm
    return render(request, "catalog/special-offers/add_special_offer.html", {"form": form})


def edit_special_offer(request, pk):
    special_offer_obj = get_object_or_404(SpecialOffers, id=pk)
    if request.method == "POST":
        form = SpecialOffersForm(
            request.POST, request.FILES, instance=special_offer_obj, error_class=DivErrorList
        )
        if form.is_valid():
            special_offer = form.save(commit=False)
            special_offer.user = request.user.supplier.owner
            special_offer.save()
            messages.success(request, message="Offer updated successfully!")
            return redirect("catalog:load_special_offers")
    else:
        form = SpecialOffersForm(instance=special_offer_obj)
    return render(request, "catalog/special-offers/special_offer_edit.html", {"form": form})


def delete_special_offer(request, pk):
    special_offer = get_object_or_404(SpecialOffers, id=pk)
    if request.method == "POST":
        special_offer.delete()
        return redirect("catalog:load_special_offers")
    context = {"special_offer": special_offer}
    return render(request, "catalog/special-offers/special_offer_delete.html", context)
    context["catalog"] = PrintUnit.objects.filter(user=supplier)
    return render(request, "catalog/print/print_inventory.html", context)


def load_print_catalog(request):
    user = get_object_or_404(User, email=request.user.email)
    supplier = user.supplier.owner
    context = {}
    context["supplier"] = Supplier.objects.filter(owner=supplier).first()
    context["catalog"] = PrintUnit.objects.filter(user=supplier)
    return render(request, "catalog/print/print_inventory.html", context)


def add_print_unit(request):
    if request.method == "POST":
        form = PrintUnitForm(request.POST, error_class=DivErrorList)
        if form.is_valid():
            print_unit = form.save(commit=False)
            print_unit.user = request.user.supplier.owner
            print_unit.save()
            messages.success(
                request,
                message="Unit added successfully.",
            )
            return redirect("catalog:load_print_catalog")

    else:
        form = PrintUnitForm()
    return render(request, "catalog/print/add_print_unit.html", {"form": form})


def edit_print_unit(request, pk):
    print_unit_obj = get_object_or_404(PrintUnit, id=pk)
    if request.method == "POST":
        form = PrintUnitForm(
            request.POST, instance=print_unit_obj, error_class=DivErrorList
        )
        if form.is_valid():
            print_unit = form.save(commit=False)
            print_unit.user = request.user.supplier.owner
            print_unit.save()
            messages.success(request, message="Unit updated successfully!")
            return redirect("catalog:load_print_catalog")
    else:
        form = PrintUnitForm(instance=print_unit_obj)
    return render(request, "catalog/print/print_unit_edit.html", {"form": form})


def delete_print_unit(request, pk):
    print_unit = get_object_or_404(PrintUnit, id=pk)
    if request.method == "POST":
        print_unit.delete()
        return redirect("catalog:load_print_catalog")
    context = {"print_unit": print_unit}
    return render(request, "catalog/print/print_unit_delete.html", context)


def upload_print_catalog(request, **kwargs):
    if request.method == "POST":
        form = PrintUnitExcelUploadForm(
            request.POST, request.FILES, error_class=DivErrorList
        )
        if form.is_valid():
            form.save(request, form, **kwargs)
            return redirect("catalog:load_print_catalog")
    else:
        form = PrintUnitExcelUploadForm
    return render(
        request,
        "catalog/common/importexcel.html",
        {
            "form": form,
            "inventory": "print",
            "action": reverse_lazy(kwargs["action"]),
        },
    )
