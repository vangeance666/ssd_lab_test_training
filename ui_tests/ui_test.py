import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as Firefox_Service

from selenium.webdriver.firefox.options import Options

from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException
SERVER_URL = "http://app-flask-ui-test:5000"
# SERVER_URL = 'http://localhost:5000'
ID_SEARCH = "search_text"
ID_SUBMIT = "submit"

ID_SUCCESS = "success-id"
ID_DETECT_HOME = "detect-home"
ID_DETECT_SUCCESS = "success-id"

@pytest.fixture()
def test_setup():
	global driver
	options = Options()
	# options.headless = True

	s = Firefox_Service(GeckoDriverManager().install())
	driver = webdriver.Firefox(service=s, options=options)
	yield driver
	driver.quit()


def do_fill_search(driver, search_message):
	search_input = driver.find_element_by_id(ID_SEARCH)
	search_input.send_keys(search_message)

	submit_btn = driver.find_element_by_id(ID_SUBMIT)

	submit_btn.click()

def element_exist_by_id(driver, ele_id) -> bool:
	try:
		ele = driver.find_element_by_id(ele_id)
	except NoSuchElementException as e:
		return False
	return True

def test_search_xss(test_setup):
	"""TO ensure that XSS search will not go thru
	To pass, need to ensure that it stays within home page and not redirected to sucess.
	"""

	# assert True

	driver.get(SERVER_URL)
	driver.implicitly_wait(3)

	do_fill_search(driver, "<script> alert('1');</script>")

	driver.implicitly_wait(4)

	res = element_exist_by_id(driver, ID_SEARCH)
	print("res: ", res)


	assert res == True


def test_no_xss(test_setup):
	"""Test non-xss string can go redirect
	"""
	driver.get(SERVER_URL)
	driver.implicitly_wait(3)

	do_fill_search(driver, "Normal string")
	driver.implicitly_wait(4)


	res = element_exist_by_id(driver, ID_SUCCESS)

	assert res == True
	# success_ele = driver.find_element_by_id(ID_SUCCESS)



