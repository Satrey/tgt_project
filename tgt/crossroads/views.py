from django.shortcuts import render
from django_admin_geomap import geomap_context

from .models import Location


def crossroads(request):
    return render(request, 'crossroads/crossroads.html', geomap_context(Location.objects.all()))

