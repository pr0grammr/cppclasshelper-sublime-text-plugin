import sublime, sublime_plugin
from .template import Template

class CreateCppClassCommand(sublime_plugin.WindowCommand):
	'''
	class for create a C++ class with a sourcefile and headerfile
	'''
	def run(self):

		# settings
		self.settings = sublime.load_settings("cppclasshelper.sublime-settings")
		self.template_dir = sublime.packages_path() + '/' + 'cppclasshelper/templates/'

		# user enter a class name to create the class
		self.window.show_input_panel("Enter class name: ", "", self.create_class, None, None)


	def create_class(self, class_name):
		
		header_file_extension = self.settings.get('header_file_extension')

		# set source file and header file
		source_file = "{}.cpp".format(class_name)
		header_file = "{}.{}".format(class_name, header_file_extension)

		source_file_template = Template("C++ Source File")
		header_file_template = Template("C++ Header File")

		try:
			source_file_template.load(self.template_dir + 'sourcefile.template')
		except OSError as e:
			sublime.error_message("Error while loading class template: {}".format(str(e)))
			return


		# render the template
		source_file_template.render(class_name=class_name, header_file_extension=header_file_extension)



		