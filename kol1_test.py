######################################
##									##
##			github_partner:			##
##			mjuzek22				##
##									##
##									##
######################################

import unittest
from kol1 import Client

class MyTest(unittest.TestCase):


	def setUp(self):
		self.name = "Adam"
		self.surname = "Abacki"
		self.cash = 0
		self.id_number = 0

	def	test_init(self):
		self.assertEqual(self.test_instance.name, self.list_data)
		self.assertEqual(self.test_instance.surname, self.surname)
		self.assertEqual(self.test_instance.cash, self.cash)
		self.assertEqual(self.test_instance.id_number, self.id_number)
		
