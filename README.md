# C++ Class Helper Sublime Text Plugin

Sublime Text Plugin for creating/generating C++ Classes. 

## Installation

Download this repository or clone it.

```bash
$ git clone https://github.com/sawzcode/cppclasshelper-sublime-text-plugin.git
```

Copy the folder in your sublime text packages path. You can find it by clicking `Preferences` -> `Browse Packages`. 

> This package might be available at <a href="https://github.com/wbond/package_control_channel" target="_blank">package control</a> soon!

## Usage

Right-click on the folder in your sidebar, where you want to create your class and click `Create C++ Class`. Enter your classname without file extension in the input panel. After you entered the name, hit return. The sourcefile and headerfile for your class will now be created in the folder you clicked in the sidebar. 

<img src="https://raw.githubusercontent.com/sawzcode/cppclasshelper-sublime-text-plugin/master/preview.gif">

## Settings

```json
{
	"open_after_creation": true, // opens the class after creation
	"header_file_extension": "hpp" // file extension in which the headerfile is created (e.g.: hpp or h)
}
```

## License 

This plugin is published under [MIT License](https://github.com/sawzcode/cppclasshelper-sublime-text-plugin/blob/master/LICENSE)


