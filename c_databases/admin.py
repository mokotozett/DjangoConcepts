from django.contrib import admin

from .models import Article

admin.site.register(Article)


#   To view model in the Admin page:
# 1. import the model
# 2. register the model in the admin