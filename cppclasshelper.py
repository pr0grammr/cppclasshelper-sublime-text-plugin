import sublime, sublime_plugin
from .template import Template

class CreateCppClassCommand(sublime_plugin.WindowCommand):
	'''
	class for create a C++ class with a sourcefile and headerfile
	'''
	def run(self, **kwargs):

		# global settings
		self.settings = sublime.load_settings("cppclasshelper.sublime-settings")
		self.vars = self.window.extract_variables()

		self.create_directory = self.vars['file_path']

		# get folder from sidebar
		if "paths" in kwargs:
			self.create_directory = kwargs['paths'][0]

		print(self.create_directory)

		# plugin settings
		self.plugin_name = 'cppclasshelper'
		self.template_dir_name = 'templates'
		self.template_dir = "{}/{}/{}/".format(sublime.packages_path(), self.plugin_name, self.template_dir_name)

		# user enter a class name to create the class
		self.window.show_input_panel("Enter class name: ", "", self.create_class, None, None)


	def create_class(self, class_name):

		# settings variables
		header_file_extension = self.settings.get('header_file_extension')

		# set source file and header file
		source_file_name = "{}.cpp".format(class_name)
		header_file_name = "{}.{}".format(class_name, header_file_extension)

		source_file_template = Template("C++ Source File")
		header_file_template = Template("C++ Header File")

		try:
			source_file_template.load(self.template_dir + 'sourcefile.template')
			header_file_template.load(self.template_dir + 'headerfile.template')
		except OSError as e:
			sublime.error_message("Error while loading class template: {}".format(str(e)))
			return


		# render the template
		source_file_template.render(class_name=class_name, header_file_extension=header_file_extension)
		header_file_template.render(class_name=class_name)

		# file names to create
		source_file = "{}/{}".format(self.create_directory, source_file_name)
		header_file = "{}/{}".format(self.create_directory, header_file_name)

		# write files
		try:

			# write source file
			source_file_obj = open(source_file, "w+")
			source_file_obj.write(source_file_template.template)
			source_file_obj.close()

			# write header file
			header_file_obj = open(header_file, "w+")
			header_file_obj.write(header_file_template.template)
			header_file_obj.close()

		except Exception as e:
			sublime.error_message("Error while creating class: {}".format(str(e)))
		
		