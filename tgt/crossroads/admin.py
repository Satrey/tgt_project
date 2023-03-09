from django.contrib import admin
from django_admin_geomap import ModelAdmin
from .models import Location


class Admin(ModelAdmin):
    geomap_default_longitude = "65.5272"
    geomap_default_latitude = "57.1522"
    geomap_height = '100%'


admin.site.register(Location, ModelAdmin)
