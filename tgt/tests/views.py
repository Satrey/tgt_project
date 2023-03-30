from django.shortcuts import render
from .models import Theme


def tests(request):
    themes = Theme.objects.all()
    username = request.GET.get('username')
    return render(request, 'tests/tests.html', {'themes': themes})
