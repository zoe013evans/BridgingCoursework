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


	def test_cv_page_returns_correct_html(self):
		request = HttpRequest()
#A request object is what Django see's when the user
#browser asks for a page. 
		response = cv(request)
#Pass it our cv page view, which gives us a response. 
		html = response.content.decode('utf8')
	#	self.assertTrue(html.startswith('<html>'))
		self.assertIn('<title>Cv Page</title>', html)
		self.assertTrue(html.strip().endswith('</html>'))

		#self.assertTemplateUsed(response, 'cv.html')


	def test_can_save_a_POST_request(self):
		response = self.client.post('/cv', data={'item_text': 'A new list item'})
		self.assertIn('A new list item', response.content.decode())