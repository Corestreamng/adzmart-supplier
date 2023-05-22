from django.contrib import admin
from .models import User, Supplier

class UserAdmin(admin.ModelAdmin):
    readonly_fields = ("last_login", "password", "phone_no", "email")
    list_display = (
        "email",
        "first_name",
        "last_name",
        "is_active",
        "created_at",
    )
    list_filter = ("is_active",)
    search_fields = ("email", "first_name", "last_name",)
    ordering = ("-created_at",)

class SupplierAdmin(admin.ModelAdmin):
    # readonly_fields = ("owner", "company_name", "company_location", "rc_number", 'government_id')
    list_display = ("owner", "company_name", "company_location", "rc_number", 'government_id', 'is_verified')
    list_filter = ("is_verified",)
    search_fields = ("company_name", "company_location", "rc_number",)

admin.site.register(User, UserAdmin)
admin.site.register(Supplier, SupplierAdmin)
