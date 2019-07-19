import sublime, sublime_plugin, os
from sublime_lib import ResourcePath

from .method_generator.exceptions import ClassValidationException
from .method_generator.generator import Generator
from .template import Template

class CreateCppClassCommand(sublime_plugin.WindowCommand):
	'''
	class for create a C++ class with a sourcefile and headerfile
	'''
	def run(self, **kwargs):

		# plugin settings
		self.package_dir = ResourcePath.from_file_path(__file__).parent
		self.plugin_name = 'C++ Classhelper'
		self.template_dir_name = 'templates'
		# self.template_dir = "{}/{}/".format(self.package_dir, self.template_dir_name)
		self.template_dir = self.package_dir / self.template_dir_name

		# global settings
		self.settings = sublime.load_settings("C++ Classhelper.sublime-settings")
		self.vars = self.window.extract_variables()
		self.view = self.window.active_view()

		self.header_file_extension = self.settings.get('header_file_extension')

		# directory where files will be created
		print(self.vars)
		if not "file_path" in self.vars:
			self.create_directory = self.vars['folder']
		else:
			self.create_directory = self.vars['file_path']

		# get folder from sidebar
		if "paths" in kwargs:
			self.create_directory = kwargs['paths'][0]

		# user enter a class name to create the class
		self.window.show_input_panel("Enter class name: ", "", self.create_class, None, None)


	def create_class(self, class_name):

		# set source file and header file
		self.source_file_name = "{}.cpp".format(class_name)
		self.header_file_name = "{}.{}".format(class_name, self.header_file_extension)

		source_file_template = Template("C++ Source File")
		header_file_template = Template("C++ Header File")
		header_template = Template("C++ Header Style")

		try:
			source_file_template.load(self.template_dir / 'sourcefile.template')
			header_file_template.load(self.template_dir / 'headerfile.template')

			if self.settings.get('use_pragma_once'):
				header_template.load(self.template_dir / 'header-new.template')
			else:
				header_template.load(self.template_dir / 'header-old.template')

		except OSError as e:
			sublime.error_message("Error while loading class template: {}".format(str(e)))
			return


		# render the template
		source_file_template.render(class_name=class_name, header_file_extension=self.header_file_extension)
		header_file_template.render(class_name=class_name)

		# render headerfile into header style
		if self.settings.get('use_pragma_once'):
			template_vars = {'class_header_content': header_file_template.template}
		else:
			template_vars = {'class_header_content': header_file_template.template, 'class_name_uppercase': self._build_header_symbol_name(class_name)}

		header_template.render(**template_vars)

		# file names to create
		self.source_file = "{}/{}".format(self.create_directory, self.source_file_name)
		self.header_file = "{}/{}".format(self.create_directory, self.header_file_name)

		# write files
		try:

			# write header file
			header_file_obj = open(self.header_file, "w+")
			header_file_obj.write(header_template.template)
			header_file_obj.close()
			self.view.set_status('class_create_progress_header_file', 'Successfully created {}'.format(self.header_file_name))

			# write source file
			source_file_obj = open(self.source_file, "w+")
			source_file_obj.write(source_file_template.template)
			source_file_obj.close()
			self.view.set_status('class_create_progress_source_file', 'Successfully created {}'.format(self.source_file_name))

			# clear status bar
			sublime.set_timeout(self._erase_status, 5000)

			if self.settings.get('open_after_creation'):
				self.open_files()


		except Exception as e:
			sublime.error_message("Error while creating class: {}".format(str(e)))



	def open_files(self):
		'''
		open files after creation
		'''
		self.window.open_file(self.header_file)


	# helper methods
	def _erase_status(self):
		self.view.erase_status('class_create_progress_header_file')
		self.view.erase_status('class_create_progress_source_file')


	def _build_header_symbol_name(self, class_name):
		class_name += "_{}".format(self.settings.get('header_file_extension'))
		class_name = class_name.upper()

		return class_name


class GenerateMethodDefinitionCommand(sublime_plugin.WindowCommand):
	"""
	generates methods for C++ header class
	"""

	# valid header extensions to search for
	VALID_HEADER_EXTENSIONS = [
		"hpp",
		"h",
		"hh",
		"H",
		"hxx",
		"h++"
	]

	class_file = None
	method_list = None
	method_definitions = None
	method_to_insert = None
	settings = None

	NEWLINE_AFTER_TEMPLATE = False
	NEWLINE_AFTER_METHOD = False
	PLACE_CURSOR_BETWEEN_BRACKETS = False

	def run(self):

		# get filename of active view and get class name which to search the header
		vars = self.window.extract_variables()
		class_name = vars["file_base_name"]
		root_dir = vars["folder"]

		self.class_file = self._find_class(root_dir, class_name)

		self.settings = sublime.load_settings("C++ Classhelper.sublime-settings")

		# setting constants with settings
		self.NEWLINE_AFTER_TEMPLATE = self.settings.get("newline_after_template")
		self.NEWLINE_AFTER_METHOD = self.settings.get("newline_after_method")
		self.PLACE_CURSOR_BETWEEN_BRACKETS = self.settings.get("place_cursor_between_brackets")

		# find out which class header to use
		if len(self.class_file) == 1:
			self.class_file = self.class_file[0]
			self._generate_method(self.class_file)
		elif len(self.class_file) > 1:
			self.window.active_view().show_popup_menu(self.class_file, self.on_class_select)
		elif not self.class_file:
			sublime.error_message("Could not find the class header in any directory")


	def on_class_select(self, class_index):

		if class_index == -1:
			return

		self.class_file = self.class_file[class_index]

		self._generate_method(self.class_file)

	def _generate_method(self, class_file):

		with open(class_file, 'r') as file:
			source_code = file.read()


		try:
			generator = Generator(source_code)

			self.method_list = generator.generate_method_list(generator.NAMES)
			self.method_definitions = generator.generate_method_list(generator.DEFINITIONS)

			self.window.active_view().show_popup_menu(self.method_list, self.on_method_select)

		except ClassValidationException as e:
			sublime.error_message(str(e))

	def insert_method(self, method):

		method.add_option(
			"newline_after_template",
			self.NEWLINE_AFTER_TEMPLATE
		)

		method.add_option(
			"newline_after_method",
			self.NEWLINE_AFTER_METHOD
		)

		method.add_option(
			"place_cursor_between_brackets",
			self.PLACE_CURSOR_BETWEEN_BRACKETS
		)

		self.window.run_command('insert_method', {
			'method': str(method),
			'cursor_between_brackets': self.PLACE_CURSOR_BETWEEN_BRACKETS
		})

	def on_method_select(self, method_index):
		if method_index == -1:
			return

		self.method_to_insert = self.method_definitions[method_index]
		self.insert_method(self.method_to_insert)

	def _find_class(self, directory, class_name):

		class_files = []

		for root, dirs, files in os.walk(directory):
			for file in files:

				# find base filename and then iterate over valid extensions to find right file
				file_basename = file
				file = os.path.splitext(file)
				file = file[0]

				if file == class_name:
					for ext in self.VALID_HEADER_EXTENSIONS:
						if file_basename == class_name + '.' + ext:
							class_files.append(os.path.join(root, file_basename))

		return class_files


class InsertMethodCommand(sublime_plugin.TextCommand):
	"""
	insert generated method into active view
	"""

	def run(self, edit, **kwargs):

		position = self.view.sel()[0].begin()
		self.view.insert(edit, position, kwargs["method"])

		# place cursor inside brackets
		if kwargs["cursor_between_brackets"]:
			pos = self.view.sel()[0].begin() - 2
			self.view.sel().clear()
			self.view.sel().add(sublime.Region(pos))