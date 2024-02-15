"""
Connor Warner
CIS 218
2/28/24
"""

from django.db import models
from django.urls import reverse

class Restaurant(models.Model):
    """Restaurant model class"""

    name = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """String method"""
        return self.name
    
    def get_absolute_url(self):
        """get the absolute URL for a single restaurant"""
        return reverse("restaurant_detail", kwargs={"pk": self.pk})


class Review(models.Model):
    """Review model class"""

    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name="reviews"
    )
    user = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        related_name="reviews"
    )
    body = models.TextField()
    rating = models
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """String method"""
        return self.body
    
    def get_absolute_url(self):
        """get the absolute URL for a single restaurant"""
        return reverse("review_detail", kwargs={"pk": self.pk})

