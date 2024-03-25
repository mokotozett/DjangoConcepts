from django.urls import path

from . import views

urlpatterns = [
    path("", views.js_home, name="js_home"),

]

