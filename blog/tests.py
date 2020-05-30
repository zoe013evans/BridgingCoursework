from django.test import TestCase
from django.urls import resolve
from blog.views import cv
from django.http import HttpRequest

# Create your tests here.

class CVPageTest(TestCase):

	def test_root_url_resolves_to_CV_page_view(self):
		found = resolve('/cv')
		self.assertEqual(found.func, cv)

#Resolve is the function to internally resolve URL's and find 
#what view function they should map to. 
#In the tutorial it wanted to resolve to root, but we already have a
#root, so we'll resolve to a CV page. 
