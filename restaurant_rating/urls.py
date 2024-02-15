"""
Connor Warner
CIS 218
2/28/24
"""

from django.urls import path
from .views import RestaurantListView, RestaurantDetailView

urlpatterns = [
    path("restaurant/<int:pk>", RestaurantDetailView.as_view(), name="restaurant_detail"),
    path("", RestaurantListView.as_view(), name="home")
]
