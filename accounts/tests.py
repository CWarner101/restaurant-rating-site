"""
Connor Warner
CIS 218
2/28/24
"""

from django.test import TestCase
from django.urls import reverse

class RegistrationTests(TestCase):
    """Tests for login and signup"""

    def test_url_exists_at_correct_location_signupview(self):
        """Test url exists at correct location detail view"""
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)

    def test_signup_view(self):
        """Test restaurant list view"""
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sign Up")
        self.assertTemplateUsed(response, "registration/signup.html")


    def test_url_exists_at_correct_location_login(self):
        """Test url exists at correct location login"""
        response = self.client.get("/accounts/login/")
        self.assertEqual(response.status_code, 200)
