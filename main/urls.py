from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.frontpage, name='home'),
    path('contact/', views.contact, name='contact')
]
