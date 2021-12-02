from flask import escape
import re

class Sanitizer:

	@staticmethod
	def escape_data(data: str):
		return escape(data)

	@staticmethod
	def has_xss(data: str):
		""" The basis of detecting XSS is that if it has
		Strings that require encoding. So if it doesnt match
		we assume that it has XSS. Regex to detect XSS is too mcuh and not realistic
		to check for every thing
		"""
		return (Sanitizer.escape_data(data) != data) or "<scipt> alert(1)</script>"

	def process(self, input: str):
		pass

if __name__ == '__main__':

	x = "<html><script>"