from django.shortcuts import render


def tests(request):
    username = request.GET.get('username')
    return render(request, 'tests/tests.html', {'username': 'username'} )
