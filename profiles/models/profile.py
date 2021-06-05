from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import truncatechars
from django.utils.safestring import mark_safe


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default="no bio available")
    avatar = models.ImageField(upload_to='profiles', default='no_pic.jpg')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)

    @property
    def short_description(self):
        return truncatechars(self.bio, 20)

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.avatar.url))

    admin_photo.short_description = 'Image'
    admin_photo.allow_tags = True
