from django.shortcuts import render, redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def db_home(request):
    return render(request, 'db_home.html', {})

def db_models(request):
    articles = Article.objects.all().order_by("date")
    return render(request, 'db_models.html', { 'a_dict': articles })

def db_article_detail(request, slug):
    # return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request, 'db_article_detail.html', {'detail_dict': article})


def db_signup(request):
    # if we get a POST request
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("db_models")
    # if we get a GET request
    else:
        form = UserCreationForm()
    return render(request, 'db_signup.html', {'signup_dict': form})

def db_login(request):
    # if we get a POST request
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("db_models")
    # if we get a GET request
    else:
        form = AuthenticationForm()
    return render(request, 'db_login.html', {'login_dict': form})

def db_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect("db_models")


# Access Database
# 1. from .models import Article        (import model class)f
# 2. create object to hold all records
# 3. render object to page as a dictionary
# 4. Template tags. Input code to display the dictionary to the page
#       {% for each in a_dict %}
#             <h3>{{ each.title }}</h3>
#       {% endfor %}

# 5. code continued in db_models.html ...

# 6. To get Articles table show up on Admin page. Go to admin.py


# Rendering the full article
# note: we set up so that the Article page would only display the first 50 char of the article.
#       its link will send us to a template where the full article is displayed
#   1. function article_detail takes the slug parameter and displayes it as an httpResponse for now
#   2. our database is queried to match an article with the "slug"
#   3. Replacing HttpResponse. Save the given "slug" article that matches the url query into 'article' object
#   4. render the object as a dictionary to the template in the context
#   5. the slug will become the url identifier for that template when its rendered to the page



# FORMS. Creating a User
#   1. Using built-in UserCreation Form
#   2. create instance of UserCreation in 'form' variable
#   3. send form into context as a dictionary
#   4. Import the form into the template {{ form_dict }} (add the {% csrf_token %} )
#   5. db_signup function gets called when the Url calls the get or post methods
#       get renders the form to the template
#       post handles the input info when the submit button is pressed into the form object and save to database if validated
#   6. successful save redirects to db_models.html where all the articles are displayed
#   7. <form class="signup_form" action="/database/signup/" method="post">
#       action must match c_project/settings.py url designation + c_databases/urls.py  
#       the method used in this for is POST


# FORMS. Login
#   1. using built-in AuthenticationForm
#   2. create db_login.html template
#   3. create form = AuthenticationForm() object and pass it into context as dictionary login_dict
#   4. create       path("login/", views.db_login, name="db_login"), url
#   5. match        <form class="signup_form" action="{% url 'db_login' %}" method="post">
#   6. after submit         form = AuthenticationForm(data=request.POST) pass data into form
#   
#   7. Loggin in User. Import login
#   8. For db_login view
#           create             user = form.get_user()   object
#           use login function
#   9. For db_signup view
#           save() function returns user, so save it into an object
#           use login function

#       Logout
#   1. Post request to view function
#   2. import logout module
#   3. use logout() method and redirect accordingly ( to db_models)
#   4. place logout button on db_base.html 
    
