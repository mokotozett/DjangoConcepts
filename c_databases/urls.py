from django.urls import path
from django.urls import re_path as url
from . import views



urlpatterns = [
    path("", views.db_home, name="db_home"),
    path("models/", views.db_models, name="db_models"),
    path("signup/", views.db_signup, name="db_signup"),
    path("login/", views.db_login, name="db_login"),
    path("logout/", views.db_logout, name="db_logout"),


    url(r'^(?P<slug>[\w-]+)/$', views.db_article_detail, name="db_article_detail"),
]


#   NAMECAPTURING GROUP:
#   url(r'^ (   ?   P   <slug>  [\w-]   +)  /$  ', views.article_detail)
#   capture syntax "^" starting
#   ? P
#   <slug> is the parameter name we want to match
#   \w- takes any letter, number, character, or -
#   $   ending
#   catches this url and passes it to the view article_detail
#   slug: url friendly string. No spaces (use hyphens), all lowercase
#   
#   Anything we type will be returned to the user 
#   http://127.0.0.1:8000/database/whtahthahtapwoetha/
#   whtahthahtapwoetha 

