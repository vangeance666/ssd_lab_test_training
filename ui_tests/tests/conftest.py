import pytest

from selenium import webdriver

from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service


@pytest.fixture(scope="class")
def init_driver(request):
	options = Options()
	options.headless = True

	service = Service(GeckoDriverManager().install())

	web_driver = webdriver.Firefox(service=service
		, options=options)

	request.cls.driver = web_driver
	web_driver.implicitly_wait(10)
	yield
	web_driver.close()
