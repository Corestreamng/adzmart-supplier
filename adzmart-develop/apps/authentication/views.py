from django.views import View
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, render, reverse, get_object_or_404
from django.contrib import messages
from django.views.generic import CreateView
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordResetForm,
    SetPasswordForm,
)
from django.urls import reverse_lazy
from django.conf import settings
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
import logging
from django.db import IntegrityError

from .form import SupplierSignUpForm, AddStaffForm, StaffUserRegForm
from .models import User, Supplier, Invitation
from .tokens import generate_account_activation_token, generate_account_setup_token
from .utilities import EmailThread
from apps.catalog.utilities import DivErrorList

log = logging.getLogger(__name__)


def notify(request, user):
    context = {
        "user": user,
        "email_activation_link": request.build_absolute_uri(
            reverse(
                "authentication:activate",
                kwargs={
                    "uidb64": urlsafe_base64_encode(force_bytes(user.pk)),
                    "token": generate_account_activation_token.make_token(user),
                },
            )
        ),
    }

    html_content = get_template(
        "authentication/email/signup-verification-email.html"
    ).render(context)
    text_content = get_template(
        "authentication/email/signup-verification-email.txt"
    ).render(context)
    mail_message = EmailMultiAlternatives(
        subject="Verification Required", body=text_content, to=[user.email]
    )
    mail_message.attach_alternative(html_content, "text/html")
    try:
        mail_message.send()
        messages.success(
            request, "You're almost done. Check your email to activate your account."
        )
    except:
        log.error("Error sending email", exc_info=1)


class SupplierRegister(CreateView):
    form_class = SupplierSignUpForm
    template_name = "authentication/supplier_register.html"
    success_url = reverse_lazy("authentication:login")

    def form_valid(self, form):
        user = form.save()

        company_name = form.cleaned_data.get("company_name")
        company_location = form.cleaned_data.get("company_location")
        rc_number = form.cleaned_data.get("rc_number")
        govt_id = form.cleaned_data.get("government_id")

        supplier = Supplier.objects.create(
            owner=user,
            company_name=company_name,
            company_location=company_location,
            rc_number=rc_number,
            government_id=govt_id,
        )
        user.supplier = supplier
        user.save()
        notify(request=self.request, user=user)

        return super().form_valid(form)


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user and user.is_verified:
                login(request, user)
                return redirect("/")
            elif user:
                notify(request, user)
        else:
            messages.info(request, "Email or Password incorrect.")
    else:
        form = AuthenticationForm(request)

    return render(request, "authentication/login.html", context={"form": form})


def activate_account(request, uidb64, token):
    uid = urlsafe_base64_decode(uidb64).decode()
    user = User.objects.get(pk=uid)

    if generate_account_activation_token.check_token(user, token):
        user.is_verified = True
        user.save()
        messages.success(request, "Email Confirmation Successful!")
    else:
        messages.error(request, "Email verification link is invalid!.")
    return redirect(settings.LOGIN_URL)


def forgot_password(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)

        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data["email"].lower()
            associated_user = User.objects.filter(email=data)

            if associated_user.exists():
                user = associated_user.first()
                context = {
                    "user": user,
                    "password_reset_url": request.build_absolute_uri(
                        reverse(
                            "authentication:password_reset_confirm",
                            kwargs={
                                "uidb64": urlsafe_base64_encode(force_bytes(user.pk)),
                                "token": generate_account_activation_token.make_token(
                                    user
                                ),
                            },
                        )
                    ),
                }

                html_content = get_template(
                    "authentication/email/forgot-password-email.html"
                ).render({"context": context})
                text_content = get_template(
                    "authentication/email/forgot-password-email.txt"
                ).render({"context": context})
                subject = "Adzmart Account Password Reset"

                try:
                    email = EmailMultiAlternatives(
                        subject=subject,
                        body=text_content,
                        from_email=None,
                        to=[user.email],
                    )
                    email.attach_alternative(html_content, "text/html")
                    EmailThread(email).start()
                    messages.success(
                        request,
                        "Email sent successfully. Check your inbox/spam folder and follow the instructions to reset your password.",
                    )
                except Exception as e:
                    messages.error(request, e)
            else:
                messages.error(
                    request,
                    "Email supplied does not exist. Kindly check and try again.",
                )

    password_reset_form = PasswordResetForm()
    return render(
        request,
        "authentication/forgot-password.html",
        context={"password_reset_form": password_reset_form},
    )


def password_reset_confirm(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    form_edit_password = SetPasswordForm(user)
    if request.method == "POST":
        form_edit_password = SetPasswordForm(user, data=request.POST)
        if form_edit_password.is_valid():
            user.is_verified = True
            form_edit_password.save()
            messages.success(
                request,
                "Password changed successfully. You can now login to your account.",
            )
            return redirect(settings.LOGIN_URL)
    return render(
        request,
        "authentication/password-reset-confirm.html",
        context={"form_edit_password": form_edit_password},
    )


def send_invitation_email(request, user, supplier):
    """
    Invitation Email/link to complete account setup for a staff user.
    """
    context = {
        "user": user,
        "supplier": supplier,
        "email_activation_link": request.build_absolute_uri(
            reverse(
                "authentication:setup_invite_account",
                kwargs={
                    "uidb64": urlsafe_base64_encode(force_bytes(user.pk)),
                },
            )
        ),
    }
    html_content = get_template(
        "authentication/email/staff-user-verification.html"
    ).render({"context": context})
    text_content = get_template(
        "authentication/email/staff-user-verification.txt"
    ).render({"context": context})
    subject = "Adzmart Account Verification"

    try:
        email = EmailMultiAlternatives(
            subject=subject, body=text_content, from_email=None, to=[user.email]
        )
        email.attach_alternative(html_content, "text/html")
        EmailThread(email).start()
        messages.success(request, message="Invite sent successfully!")
    except Exception as e:
        log.error("Error sending invitation email", exc_info=1)
        messages.error(request, e)


def add_staff_user(request):
    if request.method == "POST":
        form = AddStaffForm(request.POST, error_class=DivErrorList)
        if form.is_valid():
            try:
                staff_user = form.save(commit=False)
                user = get_object_or_404(User, email=request.user.email)
                supplier = user.supplier
                # supplier = Supplier.objects.get(owner=request.user)
                staff_user.supplier = supplier

                staff_user.status = "Pending"
                staff_user.save()
                send_invitation_email(request, staff_user, supplier)
                return redirect("catalog:pending_invite")
            except IntegrityError:
                messages.error(
                    request,
                    f"Invitation for {form.clean_email()} already exists. Please check your pending invites.",
                )
    else:
        form = AddStaffForm()
    return render(request, "catalog/staffs/add_staff_user.html", {"form": form})


def staff_invite_setup(request, uidb64):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Invitation.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    context = {"user": user, "company_name": user.supplier.company_name}
    return render(
        request, "authentication/staff-invitation/staff-invite-setup.html", context
    )


def notify_rejection_status(request, user):
    context = {
        "user": user.supplier.owner,
        "staff_name": f"{user.first_name} {user.last_name}",
    }
    html_content = get_template(
        "authentication/email/staff-rejection-email.html"
    ).render(context)
    text_content = get_template(
        "authentication/email/staff-rejection-email.txt"
    ).render(context)

    supplier_email = user.supplier.owner.email

    mail_message = EmailMultiAlternatives(
        subject="Staff Invite Rejected", body=text_content, to=[supplier_email]
    )
    mail_message.attach_alternative(html_content, "text/html")
    try:
        mail_message.send()
    except:
        log.error("Error sending email", exc_info=1)


def reject_staff_invitation(request, uuid):
    try:
        user = Invitation.objects.get(uuid=uuid)
        user.status = "Rejected"
        notify_rejection_status(request, user)
        user.save()
        messages.info(request, "You have successfully rejected this invite.")
    except (TypeError, ValueError, OverflowError, User.DoesNotExist) as e:
        user = None
        messages.error(request, str(e))
    return redirect(settings.LOGIN_URL)


class CreateStaffUser(View):
    form_class = StaffUserRegForm
    template_name = "authentication/staff-invitation/staff-user-reg.html"

    def get(self, request, uuid, *args, **kwargs):
        user = Invitation.objects.get(uuid=uuid)
        user.status = "Active"
        user.save()
        form = self.form_class(instance=user)
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        query_dict = request.POST.copy()
        supplier = Supplier.objects.filter(owner=query_dict["supplier"]).first()
        exisiting_staff_user = User.objects.filter(email=query_dict["email"]).first()
        password = query_dict["password"]

        if not exisiting_staff_user:
            staff_user = User.objects.create(
                email=query_dict["email"],
                first_name=query_dict["first_name"],
                last_name=query_dict["last_name"],
                phone_no=query_dict["phone_no"],
            )
            staff_user.set_password(password)
            staff_user.is_active = True
            staff_user.is_verified = True
            staff_user.supplier = supplier
            staff_user.save()
            messages.success(
                request,
                "Registration successful. You can now login to your account.",
            )
            return redirect(settings.LOGIN_URL)

        return render(request, self.template_name)


def logout_view(request):
    logout(request)
    return redirect(settings.LOGIN_URL)
