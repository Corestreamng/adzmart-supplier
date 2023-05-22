from django.contrib import admin
from .models import MediaBrief, MediaAdvisory, Support


class MediaBriefAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','media_type', 'location', 'duration')
    search_fields = ('company_name', 'first_name', 'last_name')


class MediaAdvisoryAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','media_type', 'planned_budget')
    search_fields = ('company_name', 'first_name', 'last_name')


class SupportAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'company_name', 'request_info')
    search_fields = ('company_name', 'first_name', 'last_name')


admin.site.register(MediaBrief, MediaBriefAdmin)
admin.site.register(MediaAdvisory, MediaAdvisoryAdmin)
admin.site.register(Support, SupportAdmin)
