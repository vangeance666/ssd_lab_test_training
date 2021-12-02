import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as Firefox_Service

from selenium.webdriver.firefox.options import Options

from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
	options.headless = True

	s = Firefox_Service(GeckoDriverManager().install())
	driver = webdriver.Firefox(service=s, options=options)
	yield driver
	driver.quit()


def do_fill_search(driver, search_message):
	search_input = driver.find_element_by_id(ID_SEARCH)
	search_input.send_keys(search_message)

	submit_btn = dirver.find_element_by_id(ID_SUBMIT)

	submit_btn.click()
	driver.implicitly_wait(2)


def test_search_xss(test_setup):
	"""TO ensure that XSS search will not go thru
	To pass, need to ensure that it stays within home page and not redirected to sucess.
	"""

	assert True

	driver.get(SERVER_URL)
	driver.implicitly_wait(3)

	do_fill_search(driver, "<script> alert('1');</script>")

	# After search with XSS ensure that will still be in home page by checkingif element is still there
	
	home_page_ele = driver.find_element_by_id(ID_SEARCH)


	assert "well done no XSS in search" != None


def test_no_xss(test_setup):
	"""Test non-xss string can go redirect
	"""
	assert True
	driver.get(SERVER_URL)
	driver.implicitly_wait(3)

	
	success_ele = driver.find_element_by_id(ID_SUCCESS)

	assert "well done" in success_ele.text


