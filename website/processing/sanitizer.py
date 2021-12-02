from flask import escape

class Sanitizer:

	@staticmethod
	def escape_data(data: str):
		return escape(data)

	def process(self, input: str):
		pass

if __name__ == '__main__':

	x = "<html><script>"

	print(has_xss(x))
	print("x: ", x)

	print(Sanitizer.escape_data(x))
