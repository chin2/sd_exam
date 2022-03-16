from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.login,name="login"),
    path('signup',views.signup,name="signup"),
    #trust_admin_login
    path('trust_admin_login/',views.trust_admin_login,name="trust_admin_login"),
    path('addimage/',views.addimage,name="addimage"),
    path('listofwhatwedo/',views.listofwhatwedo,name="listofwhatwedo"),

    path('addwhatwedo/',views.addwhatwedo,name="addwhatwedo"),
    path('headingcontentimage/',views.headingcontentimage,name="headingcontentimage"),
    path('managephotos/',views.managephotos,name="managephotos"),
    path('frontimagechange/',views.frontimagechange,name="frontimagechange"),
    path('contactusform/',views.contactusform,name="contactusform"),


    path('sample/',views.sample,name="sample"),

    path('contactusform_sumbit/',views.contactusform_sumbit,name="contactusform_sumbit"),
    path('frontimage_sumbit/',views.frontimage_sumbit,name="frontimage_sumbit"),
    path('addwhatwedo_submit/',views.addwhatwedo_submit,name="addwhatwedo_submit"),
    path('headingcontentimage_submit/',views.headingcontentimage_submit,name="headingcontentimage_submit"),
    path('listdelete/',views.listdelete,name="listdelete"),
    path('imagedelete/',views.imagedelete,name="imagedelete"),
]

