"""
Connor Warner
CIS 218
2/28/24
"""

from django.urls import path
from .views import RestaurantListView, RestaurantDetailView, ReviewDetailView, ReviewCreateView, ReviewUpdateView, ReviewDeleteView

urlpatterns = [
    path("review/create/", ReviewCreateView.as_view(), name="review_create"),
    path("restaurant/<int:pk>/", RestaurantDetailView.as_view(), name="restaurant_detail"),
    path("review/<int:pk>/", ReviewDetailView.as_view(), name="review_detail"),
    path("review/<int:pk>/update/", ReviewUpdateView.as_view(), name="review_update"),
    path("review/<int:pk>/delete/", ReviewDeleteView.as_view(), name="review_delete"),
    path("", RestaurantListView.as_view(), name="home")
]
