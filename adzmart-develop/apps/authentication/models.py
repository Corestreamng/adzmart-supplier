from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from adzmart.base_model import BaseModel


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        """Create and return a `User` with an email and password."""

        if email is None:
            raise ValueError("Email is required.")

        user = self.model(
            email=self.normalize_email(email),
            first_name=kwargs.get("first_name"),
            last_name=kwargs.get("last_name"),
            phone_no=kwargs.get("phone_no"),
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(
        self,
        email,
        password,
        first_name=None,
        last_name=None,
        phone_no=None,
    ):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        if password is None:
            raise ValueError("Superusers must have a password.")
        if email is None:
            raise ValueError("Superusers must have an email.")
        if first_name is None:
            raise ValueError("Superusers must have a first name.")
        if last_name is None:
            raise ValueError("Superusers must have a last name.")
        if phone_no is None:
            raise ValueError("Superusers must have a phone number.")

        user = self.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            phone_no=phone_no,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    email = models.EmailField(db_index=True, unique=True, null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100, blank=True, null=True)
    phone_no = models.CharField(max_length=50, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "phone_no"]

    objects = UserManager()

    def __str__(self):
        return f"{self.email}"


def user_directory_path(instance, filename):
    return 'verification/user_{0}/{1}'.format(instance.owner.id, filename)


class Supplier(BaseModel):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name="supplier_user")
    company_name = models.CharField(max_length=255, null=True, blank=True, unique=True)
    company_location = models.CharField(max_length=255, null=True, blank=True)
    rc_number = models.CharField(max_length=50, null=True, blank=True, unique=True, verbose_name='RC Number')
    government_id = models.FileField(upload_to=user_directory_path, verbose_name='Government ID')
    is_verified = models.BooleanField(default=False, verbose_name="Verified")

    def __str__(self):
        return f"{self.owner}"


class Invitation(BaseModel):
    INVITE_STATUS = (
        ('Pending', 'Pending'),
        ('Active', 'Active'),
        ('Rejected', 'Rejected')
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=INVITE_STATUS, default='Pending')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['email', 'supplier'], name='email_supplier_unique')
        ]

    def __str__(self):
        return f"{self.email}"
