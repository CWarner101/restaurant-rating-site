"""
Connor Warner
CIS 218
2/28/24
"""

from django.shortcuts import render
from django.views.generic import ListView, DateDetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Restaurant, Review

class RestaurantListView(ListView):
    """Restaurant List View"""

    model = Restaurant
    template_name = "home.html"