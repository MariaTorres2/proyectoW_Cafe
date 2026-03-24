from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio),
    path('persona/', views.persona),
    path('propietario/', views.propietario),
]