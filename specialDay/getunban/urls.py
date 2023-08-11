from django.urls import path
from . import views

urlpatterns = [  
    path("", views.getunban, name="getunban")
]
