from django.urls import path
from . import views


urlpatterns = [
    path('mainapp/', views.home, name='home')
]
