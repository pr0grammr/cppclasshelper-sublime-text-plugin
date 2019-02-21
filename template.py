import os, sublime

class Template:

	def __init__(self, name):
		self._template = None
		self._name = name
		self._filename = None


	def load(self, filename):
		# load template file
		self._filename = str(filename)

		# reading template
		self._template = filename.read_text()
		 

	def render(self, **values):
		"""
		:values key, value for replacing template vars
		"""
		self._template = self._template.format(**values)



	@property
	def template(self):
		return self._template


		


