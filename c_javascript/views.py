from django.shortcuts import render

def js_home(request):
    return render(request, 'js_home.html', {})
