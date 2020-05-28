from django.test import TestCase
from django.urls import resolve
from blog.views import main_page

# Create your tests here.

class MainPageTest(TestCase):

	def test_root_url_resolves_to_main_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, main_page)