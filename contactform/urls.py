from django.urls import path, include
from .import views
urlpatterns = [
    path('', views.contact, name="contact"),
    path('show/', views.home, name='home'),
]