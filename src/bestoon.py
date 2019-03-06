import requests
import json

class Bestoon:

	def __init__(self, token = None):

		self.__token = token

		self.url = dict()

		self.set_urls()


	def set_token(self, token):

		self.__token = token
		

	def set_urls(self):	

		self.url['base'] = 'http://bestoon.ir'

		self.url = {
			'register'       : self.url['base'] + '/accounts/register/',
			'login'    	     : self.url['base'] + '/accounts/login/',
			'set_expense'    : self.url['base'] + '/submit/expense/',
			'set_income'     : self.url['base'] + '/submit/income/',
			'get_expenses'   : self.url['base'] + '/q/expenses/',
			'get_incomes'    : self.url['base'] + '/q/incomes/',
			'general_status' : self.url['base'] + '/q/generalstat/',
		} 


	def login(self, username, password):

		data = {'username' : username, 'password' : password}

		r = requests.post(url = self.url['login'], data = data) 

		return r.json()


	def set_expense(self, amount, text):

		data = {'token' : self.__token, 'amount' : amount, 'text' : text}

		r = requests.post(url = self.url['set_expense'], data = data) 

		return r.json()


	def set_income(self, amount, text):

		data = {'token' : self.__token, 'amount' : amount, 'text' : text}

		r = requests.post(url = self.url['set_income'], data = data) 

		return r.json()


	def get_expenses(self, number = None):

		if number is None:
			data = {'token' : self.__token}
		else:
			data = {'token' : self.__token, 'num' : number}

		r = requests.post(url = self.url['get_expenses'], data = data) 

		return json.loads(r.json())


	def get_incomes(self, number = None):

		if number is None:
			data = {'token' : self.__token}
		else:
			data = {'token' : self.__token, 'num' : number}

		r = requests.post(url = self.url['get_incomes'], data = data) 

		return json.loads(r.json())


	def get_general_status(self):

		data = {'token' : self.__token}

		r = requests.post(url = self.url['general_status'], data = data) 

		return r.json()


