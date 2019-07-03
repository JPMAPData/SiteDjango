from django.urls import path

from . import views

urlpatterns = [
    path('firstSite/index.html', views.index, name='index'),
]