from django.db import models



class Article(models.Model):
    title = models.CharField(max_length = 50)
    body = models.TextField()
    slug = models.SlugField(default="", null=False)
    date = models.DateTimeField(auto_now_add=True)  #automatically populates field when this is added to table
    thumb = models.ImageField(default="default.png", blank=True)

    def __str__(self) -> str:                       #override to custom display object
        return self.title
    
    def snippet(self):
        return self.body[:50]                       # override to see only from 0 to the 50th character displayed



# MODELS SETUP
# 1. create a class. a class represents a table in the database
# 2. python manage.py makemigrations / migrate
# 3. using Django ORM
#   python manage.py shell
#   >   from c_databases.models import Article (import Article class path)
#   >   Article (display class path correctly)
#   >   Article.objects.all()   (display all elements in table)
#   >   aobject = Article()     (create an object of the Article class)
#   >   aobject.title = "Hello Kitty"
#   >   aobject.save()          (save object to database)
#   >   ctrl Z                  (quit shell)
    
#   >   firstEntry = Article.objects.get(id=1)  (Article.objects.filter(username="skuld") if u know the field's content)
#   >   firstEntry.body = "Adding a body content"
#   >   firstEntry.save()
    

# To access Database go to views.py

# ADD thumbnail
#   1. add imageField
#   2. crate 'media' folder (in c_databases ?) 
#   3. views.py in details.html template 
#       use the article object to call the new image thumb with its url