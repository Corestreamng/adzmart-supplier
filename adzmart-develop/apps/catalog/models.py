from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.authentication.models import User
from adzmart.base_model import BaseModel
from cloudinary.models import CloudinaryField


class UnitType(BaseModel):
    """Model for a billboard catalog unit type"""

    name = models.CharField(max_length=50, blank=True, null=True, unique=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"


class Unit(BaseModel):
    """Model for a billboard catalog unit. A unit belongs to a unit type."""

    class Location(models.TextChoices):
        NORTH = "N", _("North")
        SOUTH = "S", _("South")
        EAST = "E", _("East")
        WEST = "W", _("West")
        NORTH_EAST = "NE", _("North East")
        NORTH_WEST = "NW", _("North West")
        SOUTH_EAST = "SE", _("South East")
        SOUTH_WEST = "SW", _("South West")

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user"
    )
    name = models.CharField(max_length=50, blank=True, null=True)
    unit_type = models.ForeignKey(
        UnitType, on_delete=models.CASCADE, blank=True, null=True
    )
    supplier = models.CharField(max_length=50, blank=True, null=True)
    display_name = models.CharField(max_length=50, blank=True, null=True)
    adzmart_hash = models.CharField(
        max_length=64, unique=True, default=None, null=True, blank=True
    )
    reference_id = models.CharField(
        max_length=200, verbose_name="Reference ID", unique=True, null=True, blank=True
    )
    billboard_id = models.CharField(
        max_length=200, verbose_name="Billboard ID", unique=True, null=True, blank=True
    )
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    district = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    facing = models.CharField(max_length=2, choices=Location.choices, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    unit_info = models.JSONField(null=True, blank=True)
    total = models.FloatField(blank=False, null=False, default=0.0)

    def __str__(self):
        return f"{self.name}"


class RadioUnit(BaseModel):
    """Model for a supplier radio catalog units and rates"""

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="radio_user")
    Mp_Code = models.IntegerField(blank=True, null=True)
    Vendor_Name = models.CharField(max_length=255, blank=True, null=True)
    Corporate_Name = models.CharField(max_length=255, blank=True, null=True)
    Station_Name = models.CharField(max_length=255, blank=True, null=True)
    State = models.CharField(max_length=255, blank=True, null=True)
    Media_Type = models.CharField(max_length=255, null=True, default="RD")
    Rate_Desc = models.CharField(max_length=255, blank=True, null=True)
    Time = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="e.g. 6:00am-7:00am. You can separate multiple times using comma",
    )
    Duration = models.CharField(
        max_length=255, blank=True, null=True, help_text="e.g. 10secs"
    )
    Card_Rate = models.CharField(max_length=255, blank=True, null=True)
    Nego_Rate = models.CharField(max_length=255, blank=True, null=True)
    Nego_SC = models.CharField(max_length=255, blank=True, null=True)
    Card_SC = models.CharField(max_length=255, blank=True, null=True)
    Card_VD = models.IntegerField(blank=True, null=True, default=15)
    Nego_VD = models.IntegerField(blank=True, null=True)
    Add_VD = models.IntegerField(blank=True, null=True)
    SP_Disc = models.CharField(max_length=255, blank=True, null=True)
    Agency = models.IntegerField(blank=True, null=True)
    VAT = models.FloatField(blank=True, null=True, default=7.5)
    Mon = models.CharField(max_length=50, blank=True, null=True, default="Y")
    Tue = models.CharField(max_length=50, blank=True, null=True, default="Y")
    Wed = models.CharField(max_length=50, blank=True, null=True, default="Y")
    Thur = models.CharField(max_length=50, blank=True, null=True, default="Y")
    Fri = models.CharField(max_length=50, blank=True, null=True, default="Y")
    Sat = models.CharField(max_length=50, blank=True, null=True, default="Y")
    Sun = models.CharField(max_length=50, blank=True, null=True, default="Y")
    total = models.FloatField(blank=False, null=False, default=0.0)

    def __str__(self):
        return f"{self.Vendor_Name}"


class TVUnit(BaseModel):
    """Model for a supplier TV catalog units and rates"""

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tv_user")
    Mp_Code = models.IntegerField(blank=True, null=True)
    Vendor_Name = models.CharField(max_length=255, blank=True, null=True)
    Corporate_Name = models.CharField(max_length=255, blank=True, null=True)
    Station_Name = models.CharField(max_length=255, blank=True, null=True)
    State = models.CharField(max_length=255, blank=True, null=True)
    Media_Type = models.CharField(max_length=255, null=True, default="TV")
    Rate_Desc = models.CharField(max_length=255, blank=True, null=True)
    Time = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="e.g. 6:00am-7:00am. You can separate multiple times using comma",
    )
    Duration = models.CharField(
        max_length=255, blank=True, null=True, help_text="e.g. 10secs"
    )
    Card_Rate = models.CharField(max_length=255, blank=True, null=True)
    Nego_Rate = models.CharField(max_length=255, blank=True, null=True)
    Nego_SC = models.CharField(max_length=255, blank=True, null=True)
    Card_SC = models.CharField(max_length=255, blank=True, null=True)
    Card_VD = models.IntegerField(blank=True, null=True, default=15)
    Nego_VD = models.IntegerField(blank=True, null=True)
    Add_VD = models.IntegerField(blank=True, null=True)
    SP_Disc = models.CharField(max_length=255, blank=True, null=True)
    Agency = models.IntegerField(blank=True, null=True)
    VAT = models.FloatField(blank=True, null=True, default=7.5)
    Mon = models.CharField(max_length=50, blank=True, null=True, default="Y")
    Tue = models.CharField(max_length=50, blank=True, null=True, default="Y")
    Wed = models.CharField(max_length=50, blank=True, null=True, default="Y")
    Thur = models.CharField(max_length=50, blank=True, null=True, default="Y")
    Fri = models.CharField(max_length=50, blank=True, null=True, default="Y")
    Sat = models.CharField(max_length=50, blank=True, null=True, default="Y")
    Sun = models.CharField(max_length=50, blank=True, null=True, default="Y")
    total = models.FloatField(blank=False, null=False, default=0.0)

    def __str__(self):
        return f"{self.Vendor_Name}"


class BillboardImage(models.Model):
    """Model for Billboard unit images"""

    image = CloudinaryField("image")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    reference_id = models.CharField(max_length=255, null=True, blank=True)
    image_public_id = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=["image_public_id"], name="image_public_id_idx"),
        ]

    def __str__(self):
        return f"{self.billboard_unit}"


class CinemaUnit(BaseModel):
    """Model for a supplier Cinema catalog units and rate per spot"""

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cinema_user")
    cinema = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    rate_per_spot = models.IntegerField(blank=True, null=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    total = models.FloatField(blank=False, null=False, default=0.0)

    def __str__(self):
        return f"{self.cinema}"


class SpecialOffers(BaseModel):
    """Model for suppliers and Adzmart to create special offers for all categories"""

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="special_offer_user"
    )
    title = models.CharField(
        max_length=100,
        help_text="Title of special offer campaign. e.g Online Banner Package",
        null=True,
    )
    description = models.TextField(
        null=True,
        help_text="Enter a detailed description of what the offer entails.",
    )
    services = models.TextField(
        null=True, help_text="Enter the included services for this offer"
    )
    rate = models.DecimalField(decimal_places=2, max_digits=10)
    image = CloudinaryField("image")
    

    class Meta:
        verbose_name_plural = "Special Offers"

    @property
    def image_url(self):
        return self.image.url

    def __str__(self):
        return f"{self.title}"

    
class PrintUnit(BaseModel):
    """Model for a supplier Print catalog units and rates"""
    
    class ColorType(models.TextChoices):
        COLOR = 'Color', _('Color')
        BLACK_AND_WHITE = 'Black and White', _('Black and White')

    class Coverage(models.TextChoices):
        NATIONAL = 'National', _('National')
        NORTH_EAST = 'North East', _('North East')
        NORTH_WEST = 'North West', _('North West')
        NORTH_CENTRAL = 'North Central', _('North Central')
        SOUTH_EAST = 'South East', _('South East')
        SOUTH_WEST = 'South West', _('South West')
        SOUTH_SOUTH = 'South South', _('South South')

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="print_user")
    coverage = models.CharField(max_length=20, choices=Coverage.choices, null=True)
    publisher = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=15, choices=ColorType.choices, null=True)
    size = models.CharField(max_length=50, blank=True, null=True)
    position = models.CharField(max_length=150, blank=True, null=True)
    rate = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    agency_discount = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    amount = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    vat = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.publisher}"
