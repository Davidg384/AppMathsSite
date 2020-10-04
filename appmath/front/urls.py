from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('blog', views.blog, name='blog'),
    path('projects', views.projects, name='projects'),
    path('photography', views.photography, name='photography'),
    path('about', views.about, name='about')
]
