from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_profile, name='main_profile')
]
