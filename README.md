# C++ Class Helper Sublime Text Plugin

Sublime Text Plugin for creating/generating C++ Classes.

![Downloads](https://img.shields.io/packagecontrol/dt/C++%20Classhelper.svg?color=%233a9ff5&style=flat-square) ![GitHub release](https://img.shields.io/github/release/pr0grammr/cppclasshelper-sublime-text-plugin.svg?color=%2360ce52&style=flat-square) ![Travis (.com) branch](https://img.shields.io/travis/com/pr0grammr/cppclasshelper-sublime-text-plugin/feature%2Fgenerate-method-definitions.svg?style=flat-square)

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

Right-click on the folder in your sidebar, where you want to create your class and click `Create C++ Class`. Enter your classname without file extension in the input panel. After you entered the name, hit return. The sourcefile and headerfile for your class will now be created in the folder you clicked in the sidebar. 

<img src="https://raw.githubusercontent.com/pr0grammr/cppclasshelper-sublime-text-plugin/master/preview.gif">

## Settings

```javascript
{
	"open_after_creation": true, // opens the class after creation
	"header_file_extension": "hpp", // file extension in which the headerfile is created (e.g.: hpp or h)
	"use_pragma_once": true // if set to false, alternative header style will be used
}
```

## License 

This plugin is published under [MIT License](https://github.com/sawzcode/cppclasshelper-sublime-text-plugin/blob/master/LICENSE)


