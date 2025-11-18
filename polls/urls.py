from django.urls import path #importing path function from django urls 

from . import views #form ( . = all) folder importing views modules

#variable "urlpatterns" defined here and set to array of objects 
urlpatterns = [
   
    #path_function(route , folder.function name)
    #path("index/", views.index, name="index"), route that appears in the url
    path("", views.index, name="index"),

    #adding two numbers
    path('add', views.add, name="add"),
]