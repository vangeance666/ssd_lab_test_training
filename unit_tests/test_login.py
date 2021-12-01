import unittest

class TestLabtest(unittest.TestCase):
	
	# EXP_RES = "<h2 class=\"form-signin-heading\">Login</h2>"
	# BASE_URL = "https://sharkbank.sitict.net/"

	def test_return_true(self):
		x = True
		assert x

if __name__ == '__main__':
	unittest.main()