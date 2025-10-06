from django.urls import path
from . import views

app_name = 'dogs'

urlpatterns = [
    path('', views.dog_list, name='dog_list'),
    path('<int:pk>/', views.dog_detail, name='dog_detail'),
    path('create/', views.dog_create, name='dog_create'),
    path('<int:pk>/edit/', views.dog_edit, name='dog_edit'),
    path('my-dogs/', views.my_dogs, name='my_dogs'),
]
