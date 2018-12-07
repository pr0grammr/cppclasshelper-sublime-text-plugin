import os 

class Template:

	def __init__(self, name):
		self._template = None
		self._name = name
		self._filename = None


	def load(self, filename):
		# load template file
		 self._filename = filename
		 if not os.path.isfile(self._filename):
		 	raise OSError(2, "'{filename}' not found".format(filename=filename))
		 else:

		 	# set filename
		 	# read template to string
		 	self._filename = filename

		 	# reading template
		 	template_file_obj = open(self._filename, 'r')
		 	self._template = template_file_obj.read()


	def render(self, **values):
		"""
		:values key, value for replacing template vars
		"""
		self._template = self._template.format(**values)



	@property
	def template(self):
		return self._template


		


