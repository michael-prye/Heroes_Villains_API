from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_supers),
    path('<int:pk>/', views.single_super),
]