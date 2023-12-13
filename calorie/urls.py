from django.urls import path
from .views import *

urlpatterns = [
    # path('', index, name='index'),
    path('', food_list, name='food_list'),
    path('food/add/', add_food, name='add_food'),
]