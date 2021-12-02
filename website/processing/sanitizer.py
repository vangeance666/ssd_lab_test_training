from flask import escape
import re

class Sanitizer:

	@staticmethod
	def escape_data(data: str):
		return escape(data)

	@staticmethod
	def has_xss(data: str):
		return (Sanitizer.escape_data(data) != data) or ""

	def process(self, input: str):
		pass

if __name__ == '__main__':

	x = "<html><script>"