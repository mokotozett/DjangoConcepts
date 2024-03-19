from django.urls import path

from . import views

urlpatterns = [
    path("", views.html_home, name="html_home"),

]

