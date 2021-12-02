import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as Firefox_Service

from selenium.webdriver.firefox.options import Options

from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture()
def test_setup():
	global driver
	options = Options()
	options.headless = True

	s = Firefox_Service(GeckoDriverManager().install())
	driver = webdriver.Firefox(service=s, options=options)
	yield driver
	driver.quit()

def test_search_xss(test_setup):
	ID_SEARCH = "search-text-id"
	ID_SUBMIT = "submit-btn"

	ID_SUCCESS = "success-id"

	# SERVER_URL = "http://app-flask-ui-test:5000"
	SERVER_URL = "http://localhost:5000"
	driver.get(SERVER_URL)

	driver.implicitly_wait(3)

	search_input = driver.find_element_by_id(ID_SEARCH)
	search_input.send_keys("<script>")

	submit_btn = dirver.find_element_by_id(ID_SUBMIT)


	driver.implicitly_wait(2)

	no_xss_ele = driver.find_element_by_id(ID_SUCCESS)

	assert "well done no XSS in search" in no_xss_ele
