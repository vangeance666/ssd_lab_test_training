import os

from pages.login_page import LoginPage

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PayeePage(LoginPage):

	def __init__(self, driver):
		super().__init__(driver)
		self.PAYEE_URL = self.BASE_URL + '/payee'
		self.ADDPAYEE_URL = self.BASE_URL + '/addPayee'
		self.DELETEPAYEE_URL = self.BASE_URL + '/deletePayee'

	def go_url(self):
		self.driver.get(self.PAYEE_URL)

