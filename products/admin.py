from django.contrib import admin
from .models.product import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):

    list_display = [
        'admin_photo',
        'name',
        'price',
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

    readonly_fields = ('created', 'updated' , 'admin_photo')

admin.site.register(Product, ProductAdmin)
