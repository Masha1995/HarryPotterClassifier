"""HarryPotterClassifier URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, re_path
from django.views.generic import TemplateView
from CheckTextApp import views as checkTextAppViews
from ViewBaseApp import views as viewBaseAppViews

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html")),
    path('check', checkTextAppViews.check),
    path('classes', viewBaseAppViews.allClasses),
    re_path(r'^class/(?P<class_name>\w+)', viewBaseAppViews.classArticles),
    re_path(r'^article/(?P<article_id>\w+)', viewBaseAppViews.article),
    re_path(r'^.+', TemplateView.as_view(template_name="pagenotfound.html")),
]
