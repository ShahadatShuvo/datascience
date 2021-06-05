from django.contrib import admin
from .models.csv import CSV
from .models.position import Position
from .models.sale import Sale
# Register your models here.


admin.site.register(CSV)
admin.site.register(Position)
admin.site.register(Sale)