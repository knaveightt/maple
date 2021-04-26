# maple
Minimalist Automatic Project Launching Environment

This is a small collection of loosely-related scripts that reads "project" information from a YAML file, and based on a "configuration" file, presents options using [rofi](https://github.com/davatorium/rofi) to automatically launch a set of applications or commands based on the selected project.

For context, I setup these scripts to present a Rofi menu showing project names parsed from a YAML file, and based on the project I select, it automatically launches the applications I need to work on that project based on some preset commands in a configuration file.

Requires rofi and python.

