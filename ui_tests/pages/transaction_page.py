import os

from pages.login_page import LoginPage

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TransactionPage(LoginPage):

	def __init__(self, driver):
		super().__init__(driver)
		self.TRANSHISTORY_URL = self.BASE_URL + '/transhistory'

	def go_url(self):
		self.driver.get(self.TRANSHISTORY_URL)
