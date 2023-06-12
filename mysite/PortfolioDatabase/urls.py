from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.Home, name='home'),
    path('hobbies/', views.Hobbies, name='hobbies'),
    path('contact/', views.Contact, name='contact'),
    path('portfolio/', views.Portfolio, name='portfolio')
]

