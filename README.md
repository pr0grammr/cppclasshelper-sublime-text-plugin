# C++ Class Helper Sublime Text Plugin

Sublime Text Plugin for creating/generating C++ Classes and since version 1.2.0 generate definitions for your C++ class methods.

<a href="https://packagecontrol.io/packages/C%2B%2B%20Classhelper" target="_blank"><img src="https://img.shields.io/packagecontrol/dt/C++%20Classhelper.svg?color=%233a9ff5&style=flat-square"></a> <a href="https://github.com/pr0grammr/cppclasshelper-sublime-text-plugin/releases/latest"><img src="https://img.shields.io/github/release/pr0grammr/cppclasshelper-sublime-text-plugin.svg?color=%2360ce52&style=flat-square"></a> <img src="https://travis-ci.org/pr0grammr/cppclasshelper-sublime-text-plugin.svg?branch=master&style=flat-square">

## Installation

### Package Control
Install package via package control. Type <kbd>CTRL</kbd>+<kbd>SHIFT</kbd>+<kbd>P</kbd> on Windows or <kbd>CMD</kbd>+<kbd>SHIFT</kbd>+<kbd>P</kbd> on macOS and select `Package Control: Install Package` and search for `C++ Classhelper`

### Manual
Download or clone this repository.

```bash
$ git clone https://github.com/pr0grammr/cppclasshelper-sublime-text-plugin.git
```

Rename the downloaded folder to `C++ Classhelper`.
Copy the folder in the sublime text package directory. You'll find it by clicking `Preferences` -> `Browse Packages`. 


## Usage


### Class generation
Right-click on the folder in your sidebar, where you want to create your class and click `Create C++ Class`. Enter your classname without file extension in the input panel. After you entered the name, hit return. The sourcefile and headerfile for your class will now be created in the folder you clicked in the sidebar. 

<img src="https://raw.githubusercontent.com/pr0grammr/cppclasshelper-sublime-text-plugin/master/class-generation.gif">

### Class method generation

Since version **1.2.0** you are able to generate definitions for your class methods.

<img src="https://github.com/pr0grammr/cppclasshelper-sublime-text-plugin/raw/master/method-definition.gif">

Press <kbd>CTRL</kbd> + <kbd>SHIFT</kbd> + <kbd>P</kbd> to open command palette. Type in `C++ Classhelper - Generate Method Definition` (or right click in your current window to select the option via context menu) and select the method you want to generate the definition. 

## Settings

```javascript
{
    // opens the class after creation
	"open_after_creation": true,
	
	// file extension in which the headerfile is created (e.g.: hpp or h)
	"header_file_extension": "hpp",
	
	// if set to false, alternative header style will be used
	"use_pragma_once": true 
	
	// inserts a newline after every template
	"newline_after_template": true,
	
	// inserts newline after method definitions
	// curly brackets will be placed to the next line
	"newline_after_method": true,
	
	// places the cursor inside the brackets, so you can directly start typing
	"place_cursor_between_brackets": true
}
```

## License 

This plugin is published under [MIT License](https://github.com/sawzcode/cppclasshelper-sublime-text-plugin/blob/master/LICENSE)


