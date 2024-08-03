from . import views
from django.urls import path

urlpatterns = [
    path("",views.web, name = "webpage"),
    path('', views.accident_list, name='accident-list'),
]
