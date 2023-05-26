from django.urls import path
from .views import *

urlpatterns = [
    path('<slug>/', get_product, name="products"),
    path('categories/', categories, name="categories"),
]