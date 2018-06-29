from django.urls import path
from . import views

urlpatterns = [
    # ex: /
    path('', views.home_page, name='home_page'),
]
