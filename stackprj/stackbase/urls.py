from django.urls import path
from .import views

app_name='stackbase'

urlpatterns =[
    path('',views.home, name="home"),
    path('base/',views.base, name="base"),

    
   
]
