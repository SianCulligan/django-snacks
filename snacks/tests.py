from django.test import SimpleTestCase
from django.urls import reverse

class SnackTest(SimpleTestCase):
# TO RUN TESTS, USE PYTHON MANAGE.PY TEST

# *******************HOME**********************
    def test_home_page(self):
        # naming convention 'home' MUST be the same as what's in snack url.py
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_page_template(self): 
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'home.html')

# *******************ABOUT**********************
    def test_about_page(self):
        # naming convention 'home' MUST be the same as what's in snack url.py
        url = reverse('about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_about_page_template(self): 
        url = reverse('about')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'about.html')