from django.contrib import admin
from .models.profile import Profile
from django.utils.translation import ugettext_lazy as _
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):

    list_display = [
        'admin_photo',
        'user',
        'created',
        'updated',
    ]
    list_display_links = [
        'user',
    ]
    list_filter = [
        'created',

    ]
    date_hierarchy = 'created'

    readonly_fields = ('created', 'updated' , 'admin_photo')


admin.site.register(Profile, ProfileAdmin)