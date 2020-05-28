from selenium import webdriver 
import unittest


class NewVisitorTest(unittest.TestCase):

	#Tests are organised into classes
	#These will inherit from unittest.TestCase

	def setUp(self):
		self.browser = webdriver.Chrome('C:\\Program Files\\ChromeDriver\\chromedriver.exe')


	def tearDown(self):
		self.browser.quit()


	# Basically, setUp and tearDown are special methods.
	#They get run at the start and end of each test. 
	#SetUp is to open a browser and TearDown is to end it 
	#when the test ends. woo. 


	def test_can_start_a_test_and_retrieve_it_later(self):
		self.browser.get('http://localhost:8000')


		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the test!')


if __name__ == '__main__':
	unittest.main(warnings='ignore')