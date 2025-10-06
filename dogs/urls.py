from django.urls import path
from . import views

app_name = 'dogs'

urlpatterns = [
    path('', views.dog_list, name='dog_list'),
]
