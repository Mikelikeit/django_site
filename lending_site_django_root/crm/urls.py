from django.urls import path
from . import views

urlpatterns = [
    path('', views.thanks_page, name='thanks_page'),
]
