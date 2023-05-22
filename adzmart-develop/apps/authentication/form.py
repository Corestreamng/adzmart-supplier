from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import User, Supplier, Invitation
from apps.catalog.utilities import validate_file_size


class SupplierSignUpForm(UserCreationForm):
    """
    Signup Form for a supplier or agent on adzmart.
    """

    email = forms.EmailField(label="Email", required=True)
    first_name = forms.CharField(label="First Name", required=True)
    last_name = forms.CharField(label="Last Name", required=True)
    phone_no = forms.CharField(label="Phone", required=True)
    company_name = forms.CharField(label="Company Name", required=True)
    company_location = forms.CharField(label="Company Location", required=True)
    rc_number = forms.CharField(
        label="RC Number",
        required=True,
        help_text="Enter a valid company registration number",
    )
    government_id = forms.FileField(
        validators=[validate_file_size],
        label="Upload a valid government issued ID",
        required=True,
        help_text="e.g Intl passport, Voters card, Drivers License",
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            "email",
            "first_name",
            "last_name",
            "phone_no",
            "company_name",
            "company_location",
            "rc_number",
            "government_id",
        )

    def clean_email(self):
        email = self.cleaned_data.get("email").lower()
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already exists")
        return email

    def clean_company_name(self):
        company_name = self.cleaned_data.get("company_name")
        if Supplier.objects.filter(company_name=company_name).exists():
            raise ValidationError("Company already exists")
        return company_name

    def clean_rc_number(self):
        rc_number = self.cleaned_data.get("rc_number")
        if Supplier.objects.filter(rc_number=rc_number).exists():
            raise ValidationError("Company RC already exists")
        return rc_number


class AddStaffForm(forms.ModelForm):
    """
    Form for a supplier to invite a staff user
    """

    email = forms.EmailField(label="Email", required=True)
    first_name = forms.CharField(label="First Name", required=True)
    last_name = forms.CharField(label="Last Name", required=True)
    phone_no = forms.CharField(label="Phone", required=True)

    class Meta:
        model = Invitation
        fields = ("email", "first_name", "last_name", "phone_no")

    def clean_email(self):
        email = self.cleaned_data.get("email").lower()
        if User.objects.filter(email=email).exists():
            raise ValidationError(
                "The invitation process could not be completed as email already exists."
            )
        return email


class StaffUserRegForm(forms.ModelForm):
    email = forms.EmailField(label="Email", required=True)
    first_name = forms.CharField(label="First Name", required=True)
    last_name = forms.CharField(label="Last Name", required=True)
    phone_no = forms.CharField(label="Phone", required=True)
    supplier = forms.IntegerField(widget=forms.HiddenInput())
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "phone_no", "supplier")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs["readonly"] = True

    def clean(self):
        cleaned_data = super(StaffUserRegForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        email = cleaned_data.get("email")

        if password != confirm_password:
            raise ValidationError("Password and Confirm password does not match.")

        if User.objects.filter(email=email).exists():
            raise ValidationError(
                "The invite process could not be completed as email already exists."
            )
