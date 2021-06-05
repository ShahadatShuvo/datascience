from django.db import models
from django.utils.safestring import mark_safe


class Product(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='products', default='no_pic.jpg')
    price = models.FloatField(help_text='in US dollars $')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.image.url))

    admin_photo.short_description = 'Image'
    admin_photo.allow_tags = True
