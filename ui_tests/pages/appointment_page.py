import os


from pages.login_page import LoginPage

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AppointmentPage(LoginPage):

	def __init__(self, driver):
		super().__init__(driver)

		self.APPOINTMENT_URL = self.BASE_URL + '/appointment'
		self.STOREAPPT_URL = self.BASE_URL + '/storeAppt'		
		self.APPTCONFIRM_URL = self.BASE_URL + '/apptConfirm'

	def go_url(self):
		self.driver.get(self.APPOINTMENT_URL)