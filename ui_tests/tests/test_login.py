import pytest

from pages.login_page import LoginPage
from tests.test_base import BaseTest

import sys

class TestLogin(BaseTest):


	def test_login_element_exists(self):
		assert True

	# def test_signin_test_account(self):

	# 	login_page = LoginPage(self.driver)
	# 	login_page.go_url()
	# 	login_page.do_valid_login()

	# 	print("Page source: ", self.driver.page_source)

	# 	login_page.wait_dashboard()

	# 	assert login_page.get_is_reach_dashboard()

	# def test_signin_invalid_account(self):

	# 	login_page = LoginPage(self.driver)
	# 	login_page.go_url()
	# 	login_page.do_invalid_login()
	# 	login_page.wait_login_error()
	# 	assert login_page.get_is_login_fail()
		

	# def test_sql_inject_login(self):

	# 	login_page = LoginPage(self.driver)
	# 	login_page.go_url()
	# 	login_page.do_sql_inject_login()

	# 	print("Page source: ", self.driver.page_source)

	# 	login_page.wait_login_error()
	# 	assert login_page.get_is_login_fail()

	# def test_ipban_mechanism_login(self):

	# 	login_page = LoginPage(self.driver)
	# 	login_page.go_url()

	# 	INCORRECT_ROUNDS = 10

	# 	for i in range(INCORRECT_ROUNDS):
	# 		login_page.do_invalid_login()
	# 		login_page.wait_login_error()

	# 	login_page.go_url()

	# 	assert login_page.get_is_ip_blocked()

	# def test_common_passwords_login(self):
	# 	user = "admin"
	# 	common_pass = ["admin", "password","123456","12345678","1234"]

	# 	incorrect_counts = 0

	# 	login_page = LoginPage(self.driver)

	# 	for p in common_pass:
	# 		login_page.do_login_procedure(
	# 			username=user
	# 			, password=p)

	# 		login_page.wait_login_error()

	# 		if login_page.get_is_login_fail():
	# 			incorrect_counts += 1

	# 	assert incorrect_counts == len(common_pass)


