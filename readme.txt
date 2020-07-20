//////////////////////////////////////////////
##      PART I: how to use users app       ##
/////////////////////////////////////////////

users app is build to provide custom sign up, login, log out feature with custom user model. THe new custom
user model has uuid as primary key and user can log in through email. I have tried to make ready to go app
however, there are some cutomization that you want to make like, where to redirect a user if he/she is logged
in. So to do that follow following steps:

first of all read this, why we should do this (first paragraph is enough) -
https://learndjango.com/tutorials/django-custom-user-model

steps:
1.  As django's official docs says -
https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project
if you want to create custom user model( which you shoul be, because in future you may want to extend user
fiels) you should do it before initial migrations. i.e. before running the server for the first time, you
should make these changes.

1.1 In case you have already run the migrations, either delete the db and initial migrations or follow this
link - https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#changing-to-a-custom-user-model-mid-project

2.  Now we need to update the path for redirection
    A.  your_project_name/settings/base.py
        LOGIN_REDIRECT_URL = 'home'
        LOGOUT_REDIRECT_URL = 'home'

        as you can see here, by default path of login and log out is {{ url 'home' }},
        you'can update it. Here, 'home' is namespacing of a url which renders 'users/home' template.
3.  You have to update root urls.py i.e. your_project_name/urls.py

    from django.contrib import admin
    from django.urls import path, include
    from django.contrib.auth import views as auth_views
    from django.views.generic.base import TemplateView

    urlpatterns = [
        path('', TemplateView.as_view(template_name='users/home.html'), name='home'),
        path('admin/', admin.site.urls),
        path('users/', include('users.urls')),
        path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
        path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    ]



////////////////////////////////////////////////
##  PART II: how to use de-coupled settings  ##
///////////////////////////////////////////////

steps:
1.  copy and paste settings folder from this project into your project directory in which
wsgi.py, asgi.py, urls.py, and __init__.py are located

2.  you need to update 3 pointers in of your project:
    A.  your_project_name/asgi.py:
            for development:
                os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings.dev')
            for production:
                os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings.prod')
    B.  your_project_name/wsgi.py:
            for development:
                os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_reusable.settings.dev')
            for production:
                os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_reusable.settings.prod')
    C.  your_project_name/settings/base.py:
            a.  ROOT_URLCONF = 'your_project_name.urls'
                e.g.
                ROOT_URLCONF = 'django_reusable.urls'
            b.  WSGI_APPLICATION = 'your_project_name.wsgi.application'
                e.g.
                WSGI_APPLICATION = 'django_reusable.wsgi.application'
    D.  you also need to update, manage.py. So in manage.py
            for development:
                os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings.dev')
            for production:
                os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings.prod')


//////////////////////////////////////////////////
##      PART III: managing secret keyies        ##
//////////////////////////////////////////////////

read this - https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/#secret-key
also, https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Deployment
watch - https://www.youtube.com/watch?v=dNxjxA4kzFI (I've followed this youtube video steps)
as official docs says,

    import os
    SECRET_KEY = os.environ['SECRET_KEY']
    or from a file:

    with open('/etc/secret_key.txt') as f:
        SECRET_KEY = f.read().strip()

the best way to do it is, do it manually.

or, just add add following lines to your_virtual_environment/bin/avtivat

export DJANGO_SECRET_KEY="9^8*...."
export SET_DEBUG="False"
and so on...

similary, add third pary API keys like, fb's, twitter's, etc.
note: there should not be any space.
now restart the virtual environment.