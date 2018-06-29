from django.urls import path
from . import views

urlpatterns = [
    # ex: /
    path('', views.homepage, name='homepage'),
    path('addFooddetail', views.add_food, name='add_food'),
    path('deleteFood', views.delete_row_table, name='delete_row_table'),
]
