from django.urls import path

from assignment1 import views

urlpatterns = [
    path("",views.send_massages,name='assignment_a'),
]