import os

from pages.login_page import LoginPage

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SupportPage(LoginPage):

	def __init__(self, driver):
		super().__init__(driver)
		self.SUPPORT_URL = self.BASE_URL + '/support'

	def go_url(self):
		self.driver.get(self.SUPPORT_URL)