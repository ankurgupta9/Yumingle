"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from home.views import home
from yumingle.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home' ),
    path('add', add_recipe, name='add_recipe' ),
    path('view', my_recipe, name='my_recipe' ),
    path('search', my_search, name='my_search' ),
    path('delete_recipe/<id>/', delete_recipe, name='delete_recipe' ),
    path('update_recipe/<id>/', update_recipe, name='update_recipe' ),
    path('recipe_detail/<id>/', recipe_detail, name='recipe_detail' ),
    # path('recipe/<id>/rate_recipe', rate_recipe, name='rate_recipe'),
    path('recipe/<id>/add_review/', add_review, name='add_review'),
    path('login',Login_page,name='Login_page'),
    path('register',Register_page,name='Register_page'),
    path('logout',Logout_page,name='Logout_page'),
]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()