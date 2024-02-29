"""
Connor Warner
CIS 218
2/28/24
"""

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Restaurant, Review

class RestaurantsTests(TestCase):
    """Restaurant Tests"""

    @classmethod
    def setUpTestData(cls):
        cls.restaurant = Restaurant.objects.create(
            name="Test Restaurant"
        )

    def test_restaurant_model(self):
        """Test restaurant model"""
        self.assertEqual(self.restaurant.name, "Test Restaurant")
        self.assertEqual(str(self.restaurant), "Test Restaurant")
        self.assertEqual(self.restaurant.get_absolute_url(), "/restaurant/1")

    def test_restaurant_url_exists_at_correct_location_listview(self):
        """Test url exists at correct location list view"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_correct_location_detailview(self):
        """Test url exists at correct location detail view"""
        #TODO: Ask why this test isn't working, but the first one is.
        response = self.client.get("/restaurant/1/")
        self.assertEqual(response.status_code, 200)

    def test_restaurant_listview(self):
        """Test restaurant list view"""
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Restaurant")
        self.assertTemplateUsed(response, "home.html")

    def test_restaurant_detailview(self):
        """Test restaurant detail view"""
        response = self.client.get(reverse("restaurant_detail", kwargs={"pk": self.restaurant.pk}))
        no_response = self.client.get("/restaurant/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Test Restaurant")
        self.assertTemplateUsed(response, "restaurant_detail.html")


class ReviewTests(TestCase):
    """Review Tests"""

    @classmethod
    def setUpTestData(cls):
        cls.restaurant = Restaurant.objects.create(
            name="Test Restaurant"
        )

        cls.user = get_user_model().objects.create_user(
            username="testuser", password="secret"
       )

        cls.review = Review.objects.create(
            restaurant= cls.restaurant,
            user = cls.user,
            body = "Test review",
            rating = 3,
        )

    def test_review_model(self):
        """Test the review model"""
        self.assertEqual(self.review.restaurant.name, "Test Restaurant")
        self.assertEqual(str(self.review), "Test review")
        self.assertEqual(self.review.rating, 3)


    def test_review_url_exists_at_correct_location_detailview(self):
        """Test url exists at correct location detail view"""
        response = self.client.get("/review/1/")
        self.assertEqual(response.status_code, 200 )
        
    def test_review_detailview(self):
        """Test review detail view"""
        response = self.client.get(reverse("review_detail", kwargs={"pk": self.restaurant.pk}))
        no_response = self.client.get("/review/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Test review")
        self.assertTemplateUsed(response, "review_detail.html")


    def test_review_url_exists_at_correct_location_createview(self):
        """Test url exists at correct location create view"""
        response = self.client.get("/review/create/")
        self.assertEqual(response.status_code, 200 )

    def test_review_createview(self):
        """Test review create view"""
        response = self.client.get(reverse("review_create"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Write a Review")
        self.assertTemplateUsed(response, "review_create.html")


    def test_review_url_exists_at_correct_location_updateview(self):
        """Test url exists at correct location update view"""
        response = self.client.get("/review/edit/")
        self.assertEqual(response.status_code, 200 )

    def test_review_createview(self):
        """Test review create view"""
        response = self.client.get(reverse("review_update", kwargs={"pk": self.review.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Restaurant - Edit Review")
        self.assertTemplateUsed(response, "review_update.html")

    
    def test_review_url_exists_at_correct_location_deleteview(self):
        """Test url exists at correct location delete view"""
        response = self.client.get("/review/delete/")
        self.assertEqual(response.status_code, 200 )

    def test_review_deleteview(self):
        """Test review delete view"""
        response = self.client.get(reverse("review_delete", kwargs={"pk": self.review.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Are you sure you want to delete this review?")
        self.assertTemplateUsed(response, "review_delete.html")

