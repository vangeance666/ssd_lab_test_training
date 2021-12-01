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

def test_login(test_setup):

	SERVER_URL = "http://app-flask-ui-test:5000"
	# driver.get("google.com")
	print(dirver.page_source)

	
	driver.get(SERVER_URL) 


	
	
	assert True
