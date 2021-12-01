import os

from pages.login_page import LoginPage

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage(LoginPage):

	def __init__(self, driver):
		super().__init__(driver)
		self.DASHBOARD_URL = self.BASE_URL + '/dashboard'


	def go_url(self):
		self.driver.get(self.DASHBOARD_URL)

