'''
Definition Generator for C++ Classes
fetch classes and included methods from class via regex
create_definition command shows a quick panel, where the user can choose the right method to insert
'''

class CppClass:
	'''
	CppClass represents a C++-Class with given name
	and included methods
	'''

	def __init__(self, name):
		self._name = name




class Method:
	'''
	represents a class method
	'''
	def __init__(self, name):
		self._name = name



