from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(ServiceModel)
class ServiceAdmin(admin.ModelAdmin):
    search_fields = ['id', 'name']
    # list_display = ['id', 'name', 'price', 'status']


@admin.register(PackageModel)
class PackageAdmin(admin.ModelAdmin):
    search_fields = ['id', 'name']
    # list_display = ['id', 'name', 'price', 'status', 'services']
