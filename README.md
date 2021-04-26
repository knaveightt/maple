# maple
Minimalist Automatic Project Launching Environment

This is a small collection of loosely-related scripts that reads "project" information from a YAML file, and based on a "configuration" file, presents options using [rofi](https://github.com/davatorium/rofi) to automatically launch a set of applications or commands based on the selected project.

For context, I setup these scripts to present a Rofi menu showing project names parsed from a YAML file, and based on the project I select, it automatically launches the applications I need to work on that project based on some preset commands in a configuration file.

Requires rofi and python.

## File Explanation
**projects** (shell script) is the script that is executed by a hotkey on my system. It calls the python script to parse my projects YAML file and call Rofi appropriately, as well as runs the commands to launch applications based on the project name selected.

**project-parse.py** is the python script I wrote to parse the project and config YAML files, and return commands / project names according to how its called via the *projects** shell script

**config.yaml** is the YAML file designed to be edited, to define where to find the projects YAML file is and what commands to associate / execute based on the projects in that file. As an example, my projects YAML file can be found [here](https://github.com/knaveightt/knaveightt.github.io/blob/gh-pages/_data/projects.yaml**

**knv-workspaces.el** is an example of an Emacs el file written that is included in my .emacs setup, that contains the function automatically called when booting up a project that I use emacs for primarily. This is an example of how to use these scripts, and show that I use this function to setup Emacs a certain way when I launch the associated project.


More documentation to follow..
