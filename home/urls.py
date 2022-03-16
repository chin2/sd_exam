from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('detailswhatwedo/',views.detailswhatwedo,name="detailswhatwedo"),
    path('sample2/',views.sample2,name="sample2")
]

