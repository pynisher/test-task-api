from django.urls import path
from . import views

urlpatterns = [
    path('encrypt/', views.encrypt),
    path('decrypt/', views.decrypt),
    path('', views.index),
]
