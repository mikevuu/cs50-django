from django.urls import path
from . import views 
urlpatterns =[
    path("",views.index,name="index"),
    path("mike", views.mike, name="mike"),
    path("<str:name>", views.greet, name = "greet")
]