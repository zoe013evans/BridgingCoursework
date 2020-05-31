from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import unittest
import time



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





	def test_can_start_a_list_and_retrieve_it_later(self):
		self.browser.get('http://localhost:8000/cv')


		#Noticing the page title and header mention CV

		self.assertIn('Cv Page', self.browser.title)
		
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Cv Page', header_text)

		#Invited to enter a to-do item straight away 

		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
			)

		#She types #buy peacock feathers into a text box

		inputbox.send_keys('Buy peacock feathers')

		#When she hits enter, the page updates, and now the page
		#lists "1: Buy peacock feathers as an item in a to-do list
		#" table

		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertTrue(any(row.text == '1: Buy peacock feathers' for row in rows),
			"New to-do item did not appear in table")


		self.fail('Finish the test')


if __name__ == '__main__':
	unittest.main(warnings='ignore')
	#This is how a python script checks it's been executed
	#from the commandline, rather than another script. 
