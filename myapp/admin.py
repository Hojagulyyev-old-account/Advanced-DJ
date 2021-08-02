from django.contrib import admin
from .models import Product, SoftInfo, HardInfo, Item
# Register your models here.

admin.site.register(Product)
admin.site.register(SoftInfo)
admin.site.register(HardInfo)
admin.site.register(Item)
