######################################
##									##
##			github_partner:			##
##			mjuzek22				##
##									##
##									##
######################################

import unittest
import kol1
import kol1dodek08

class Client2Test(unittest.TestCase):

#from my program in order to provide 12 tests
	def setUp(self):
		self.client = kol1dodek08.Client("Adam", 21)

	def test_init(self):
		self.assertEquals(self.client.name,'Adam')
		self.assertEquals(self.client.id, 21)
		self.assertEquals(self.client.accounts, 0)

	def test_info(self):
		self.assertEquals(self.client.info(), ('Adam',21,0))

class SystemTest(unittest.TestCase):

#from my program in order to provide 12 tests
	def setUp(self):
		self.system = kol1dodek08.System()

	def test_init(self):
		self.assertEquals(self.system.banks, [])
		self.assertEquals(self.system.clients, [])
		self.assertEquals(self.system.number_of_banks, 0)
		self.assertEquals(self.system.number_of_clients, 0)

		


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

	def test_write_client_data(self):
		self.bank.new_client('Barbara','Babacka', 1000)
		self.bank.write_client_data('testfile')
		outfile = open('testfile',"r") 
		content = outfile.read()
		self.assertEqual(content, "Barbara Babacka : 1000\n")

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
