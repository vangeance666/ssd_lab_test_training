import os

from pages.base_page import BasePage

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# CLASS_NAME = 'class name'
# CSS_SELECTOR = 'css selector'
# ID = 'id'
# LINK_TEXT = 'link text'
# NAME = 'name'
# PARTIAL_LINK_TEXT = 'partial link text'
# TAG_NAME = 'tag name'
# XPATH = 'xpath'
# print(By.NAME)

class LoginPage(BasePage):

	TEST_VALID_USERNAME = os.environ['FLASK_UI_TEST_USERNAME']
	TEST_VALID_PASSWORD = os.environ['FLASK_UI_TEST_PASSWORD']

	TEST_INVALID_USERNAME = "GJKSENQGJKNQSEJKGJNK"
	TEST_INVALID_PASSWORD = "GJNKSANJKGANJKGSAJNKGNQWEJKGNQJK"

	BY_USERNAME 	= (By.NAME, "username")
	BY_PASSWORD 	= (By.NAME, "password")
	BY_LOGIN_FORM 	= (By.CSS_SELECTOR, "form.form.form-signin")
	BY_OTP_FORM 	= (By.CSS_SELECTOR, "form#form-otp")
	BY_LOGIN_ERROR 	= (By.CSS_SELECTOR, "div.alert.alert-danger.alert-dismissable")

	BY_LOGIN_BUTTON = (By.ID, "submit")

	BY_DASHBOARD_TITLE = (By.CSS_SELECTOR, "h1.h3.mb-0.text-gray-800")

	MSG_INCORRECT_LOGIN = "Incorrect login"

	# MSG_CORRECT_LOGIN = "2 Factor Authentication"

	MSG_CORRECT_LOGIN = "h1.h3.mb-0.text-gray-800"

	MSG_DASHBOARD_REACH = "Account Overview"

	SQL_INJECT_USERNAME = "'or'1'=1'--"
	SQL_INJECT_PASSWORD = "'or'1'=1'--"

	def __init__(self, driver):
		super().__init__(driver)

		self.LOGIN_URL = self.BASE_URL
		# self.driver.get(self.LOGIN_URL)
		
	def go_url(self):
		self.driver.get(self.LOGIN_URL)

	def get_is_reach_dashboard(self) -> bool:
		print(self.driver.page_source)
		return self.MSG_DASHBOARD_REACH in self.driver.page_source

	def get_is_ip_blocked(self) -> bool:

		return True

	def get_is_login_fail(self) -> bool:
		return self.MSG_INCORRECT_LOGIN in self.driver.page_source

	def get_is_login_success(self) -> bool:
		return self.MSG_CORRECT_LOGIN in self.driver.page_source

	def do_login_procedure(self, username: str, password: str):
		self.do_send_keys(by_locator=self.BY_USERNAME
			, text=username)

		self.do_send_keys(by_locator=self.BY_PASSWORD
			, text=password)

		self.do_click(by_locator=self.BY_LOGIN_BUTTON)

		# self.do_submit(by_locator=self.BY_LOGIN_FORM)

	def wait_dashboard(self):
		self._do_wait(EC.text_to_be_present_in_element(
			self.BY_DASHBOARD_TITLE
			, self.MSG_DASHBOARD_REACH))

	def wait_otp_form(self):
		self._do_wait(EC.visibility_of_element_located(
			self.BY_OTP_FORM))

	def wait_login_error(self):
		self._do_wait(EC.text_to_be_present_in_element(
			self.BY_LOGIN_ERROR
			, self.MSG_INCORRECT_LOGIN))

	def do_valid_login(self):
		self.do_login_procedure(self.TEST_VALID_USERNAME
			, self.TEST_VALID_PASSWORD)

	def do_invalid_login(self):
		self.do_login_procedure(self.TEST_INVALID_USERNAME
			, self.TEST_INVALID_PASSWORD)

	def do_sql_inject_login(self):
		self.do_login_procedure(self.SQL_INJECT_USERNAME
			, self.SQL_INJECT_PASSWORD)
		