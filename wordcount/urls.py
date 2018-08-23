"""wordcount URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from django.urls import path
from . import page_sans_url,page_avec_url

urlpatterns = [
    #path('',page_sans_url.fonction0),###page par default si aucune url nest donee
    #path('',page_sans_url.fonction1),###page par default si aucune url nest done avec fonction differente
    path('url3',page_avec_url.fonction3),
    path('url4',page_avec_url.fonction4),
    path('testhttp',page_avec_url.fonctionhttp),


    path('',page_avec_url.homepage,name='home'),#page par default+fonction qui renvoie vers une template html
    path('count/',page_avec_url.count,name='count'),name=count renvoie vers la meme url count
    path('about/',page_avec_url.about,name='about'),
    #path('counthe/',page_avec_url.count,name='count'),#ici on a changer lurl count mais le bouton count renvoie toujours vers la page count



]
