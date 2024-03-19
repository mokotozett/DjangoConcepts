from django.shortcuts import render

def html_home(request):
    return render(request, 'html_home.html', {})
