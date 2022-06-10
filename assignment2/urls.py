from django.contrib import admin
from django.urls import path

from assignment2 import views

urlpatterns = [
   path("",views.FirstView.as_view())
]