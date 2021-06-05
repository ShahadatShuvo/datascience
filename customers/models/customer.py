from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=30)
    logo = models.ImageField(upload_to='customers', default='np_pic.jpg')

    def __str__(self):
        return str(self.name)


