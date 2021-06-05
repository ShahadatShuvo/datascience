from django.db import models


class CSV(models.Model):
    file_name = models.FileField(upload_to='sales/csvs')
    activated = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.file_name)