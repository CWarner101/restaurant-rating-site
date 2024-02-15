from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Restaurant, Review

class RestaurantsTests(TestCase):
    """Restaurant Tests"""

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser", email="test@email.com", password="secret"
        )

        cls.restaurant = Restaurant.objects.create(
            name="Test Restaurant"
        )

    def test_restaurant_model(self):
        """Test restaurant model"""
        self.assertEqual(self.restaurant.name, "Test Restaurant")
        self.assertEqual(str(self.restaurant), "Test Restaurant")
        self.assertEqual(self.restaurant.get_absolute_url(), "/restaurant/1")

    def url_exists_at_correct_location_listview(self):
        """Test url exists at correct location list view"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def url_exists_at_correct_location_detailview(self):
        """Test url exists at correct location detail view"""
        response = self.client.get("/restaurant/1/")
        self.assertEqual(response.status_code, 200)

    def test_post_listview(self):
        """Test restaurant list view"""
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Restaurant")
        self.assertTemplateUsed(response, "home.html")

    def test_post_detailview(self):
        """Test restaurant detail view"""
        response = self.client.get(reverse("restaurant_detail", kwargs={"pk": self.restaurant.pk}))
        no_response = self.client.get("/restaurant/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Test Restaurant")
        self.assertTemplateUsed(response, "restaurant_detail.html")


class ReviewTests(TestCase):
    """Review Tests"""

    #TODO: Create Review Tests