from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# WebDriverWait returns an element if managed to wait for it

# EC stuffs
	# title_is
	# title_contains
	# presence_of_element_located
	# visibility_of_element_located
	# visibility_of
	# presence_of_all_elements_located
	# text_to_be_present_in_element
	# text_to_be_present_in_element_value
	# frame_to_be_available_and_switch_to_it
	# invisibility_of_element_located
	# element_to_be_clickable
	# staleness_of
	# element_to_be_selected
	# element_located_to_be_selected
	# element_selection_state_to_be
	# element_located_selection_state_to_be
	# alert_is_present
	 
class BasePage:

	TIMEOUT_SECS = 10
	
	def __init__(self, driver):
		self.BASE_URL = "http://shark-flask-ui-test:5000"
		# self.BASE_URL = "http://sharkbank.sitict.net"
		self.driver = driver

	def _do_wait(self, conditions):
		return WebDriverWait(self.driver
			, self.TIMEOUT_SECS).until(conditions)

	def do_click(self, by_locator):
		self._do_wait(EC.visibility_of_element_located(by_locator)).click()

	def do_send_keys(self, by_locator, text):
		element = self._do_wait(EC.visibility_of_element_located(by_locator)).send_keys(text)
		# return element.text

	def do_submit(self, by_locator):
		element = self._do_wait(EC.visibility_of_element_located(by_locator)).submit()

	def get_title(self, expected_title):
		self._do_wait(EC.title_is(expected_title))
		return self.driver.title



