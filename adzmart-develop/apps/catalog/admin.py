from django.contrib import admin
from apps.catalog.models import (
    Unit,
    UnitType,
    RadioUnit,
    TVUnit,
    BillboardImage,
    CinemaUnit,
    SpecialOffers,
)
from apps.catalog.forms import UnitFormAdmin


class UnitTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "description")


class UnitAdmin(admin.ModelAdmin):
    form = UnitFormAdmin
    list_display = (
        "name",
        "unit_type",
        "supplier",
        "reference_id",
        "billboard_id",
        "latitude",
        "longitude",
        "facing",
        "state",
        "country",
    )
    search_fields = (
        "name",
        "unit_type__name",
        "reference_id",
        "billboard_id",
        "state",
        "country",
    )
    readonly_fields = ("user",)


class RadioUnitAdmin(admin.ModelAdmin):
    list_display = (
        "Mp_Code",
        "Vendor_Name",
        "Corporate_Name",
        "Station_Name",
        "State",
        "Time",
        "Rate_Desc",
        "Duration",
        "Card_Rate",
        "Nego_Rate",
    )
    search_fields = (
        "Vendor_Name",
        "Corporate_Name",
        "Station_Name",
        "State",
        "Time",
        "Rate_Desc",
        "Duration",
    )
    readonly_fields = ("user", "Media_Type")


class TVUnitAdmin(admin.ModelAdmin):
    list_display = (
        "Mp_Code",
        "Vendor_Name",
        "Corporate_Name",
        "Station_Name",
        "State",
        "Time",
        "Rate_Desc",
        "Duration",
        "Card_Rate",
        "Nego_Rate",
    )
    search_fields = (
        "Vendor_Name",
        "Corporate_Name",
        "Station_Name",
        "State",
        "Time",
        "Rate_Desc",
        "Duration",
    )
    readonly_fields = ("user", "Media_Type")


class CinemaUnitAdmin(admin.ModelAdmin):
    list_display = ("cinema", "location", "rate_per_spot")
    search_fields = ("cinema", "location")
    readonly_fields = ("user",)


class SpecialOffersAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "services", "rate")
    search_fields = ("tile", "description", "services")
    readonly_fields = ("user",)


admin.site.register(UnitType, UnitTypeAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(RadioUnit, RadioUnitAdmin)
admin.site.register(TVUnit, TVUnitAdmin)
admin.site.register(CinemaUnit, CinemaUnitAdmin)
admin.site.register(SpecialOffers, SpecialOffersAdmin)
