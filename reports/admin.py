from django.contrib import admin
from .models.report import Report


# Register your models here.

class ReportAdmin(admin.ModelAdmin):
    list_display = [
        'admin_photo',
        'name',
        'remarks',
        'author',
        'created',
        'updated',
    ]
    list_display_links = [
        'name',
    ]
    list_filter = [
        'created',

    ]
    date_hierarchy = 'created'

    readonly_fields = ('created', 'updated', 'admin_photo')


admin.site.register(Report, ReportAdmin)
