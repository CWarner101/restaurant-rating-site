"""
Connor Warner
CIS 218
2/28/24
"""

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Restaurant, Review

class RestaurantListView(ListView):
    """Restaurant List View"""

    model = Restaurant
    template_name = "home.html"


class RestaurantDetailView(DetailView):
    """Restaurant Detail View"""

    model = Restaurant
    template_name = "restaurant_detail.html"


class ReviewDetailView(DetailView):
    """Review Detail View"""

    model = Review
    template_name = "review_detail.html"


class ReviewCreateView(CreateView):
    """Review Create View"""

    model = Review
    template_name = "review_create.html"


class ReviewUpdateView(UpdateView):
    """Review Update View"""

    model = Review
    template_name = "review_update.html"


class ReviewDeleteView(DeleteView):
    """Review Delete View"""

    model = Review
    template_name = "review_delete"