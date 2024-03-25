from django.shortcuts import render

def db_home(request):
    return render(request, 'db_home.html', {})
