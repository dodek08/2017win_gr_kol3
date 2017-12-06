######################################
##									##
##			github_partner:			##
##			mjuzek22				##
##									##
##									##
######################################

import unittest
import kol1

class ClientTest(unittest.TestCase):


	def setUp(self):
		self.client = kol1.Client("Adam","Abacki",1000,21)

	def test_init(self):
		self.assertEquals(self.client.name,'Adam')
		self.assertEquals(self.client.surname,'Abacki')
		self.assertEquals(self.client.cash, 1000)
		self.assertEquals(self.client.id_number, 21)

class  BankTest(unittest.TestCase):


	def setUp(self):
		self.bank = kol1.Bank('PKO')

	def test_init(self):
		self.assertEquals(self.bank.name,'PKO')
		self.assertEquals(self.bank.clients,[])

	def test_new_client(self):
		self.bank.new_client('Barbara','Babacka', 1000)
		self.assertEquals(self.bank.clients[0].name, 'Barbara')
		self.assertEquals(self.bank.clients[0].surname, 'Babacka')
		self.assertEquals(self.bank.clients[0].cash, 1000)
		self.assertEquals(self.bank.clients[0].id_number, 1)

	def test_client_list(self):
		self.bank.new_client('Barbara','Babacka', 1000)
		self.assertEquals(self.bank.client_list(),None)

	def test_cash_input(self):
		self.bank.new_client('Barbara','Babacka', 1000)
		self.bank.cash_input(0,100)
		self.assertEquals(self.bank.clients[0].cash, 1100)

	def test_cash_withdrawal(self):
		self.bank.new_client('Barbara','Babacka', 1000)
		self.bank.cash_withdrawal(0, 100)
		self.assertEquals(self.bank.clients[0].cash, 900)

	def test_money_transfer(self):
		self.bank.new_client('Barbara','Babacka', 1000)
		self.bank.new_client('Celina','Cabacka', 2000)
		self.bank.money_transfer(0,1,100)
		self.assertEquals(self.bank.clients[0].cash, 1100)
		self.assertEquals(self.bank.clients[1].cash, 1900)

class  TransferTest(unittest.TestCase):

	def setUp(self):
		self.transfer = kol1.Transfer()
		self.bank = kol1.Bank('PKO')
		self.bank.new_client('Barbara','Babacka', 1000)
		self.bank.new_client('Celina','Cabacka', 2000)

	def test_money_transfer(self):
		self.transfer.money_transfer('PKO', 1, 'PKO', 2, 100)
		self.assertEquals(self.bank.clients[0].cash, 900)
		self.assertEquals(self.bank.clients[1].cash, 2100)
