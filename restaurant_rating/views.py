"""
Connor Warner
CIS 218
2/28/24
"""

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

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
    fields = ["restaurant", "user", "body", "rating"]

    def get_initial(self):
        """Get initial form data"""
        # Get the result of calling the parent method
        initial_data = super().get_initial()
         # Add the author so it is the requests user
        initial_data['user'] = self.request.user
        # Return the data
        return initial_data

class ReviewUpdateView(UpdateView):
    """Review Update View"""
    model = Review
    template_name = "review_update.html"
    fields = ["restaurant", "body", "rating"]


class ReviewDeleteView(DeleteView):
    """Review Delete View"""
    model = Review
    template_name = "review_delete.html"
    success_url = reverse_lazy("home")