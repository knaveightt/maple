#!/usr/bin/env python 

# Requires pyyaml, you can install using pip
# Also import argparse
import yaml
import argparse

def load_raw_yaml_file(filename):
    """
    Loads a file and returns a string of the contents.
    Assumes the contents is YAML, and that this function is called within yaml.safe_load

    @return filename (string)
    """
    yamlstream =""
    
    with open(filename, 'r') as stream:
        # list comprehension to get entire file as list object
        lines = [line.rstrip('\n') for line in stream]
        yamlstream = "" 
        for line in lines:
            yamlstream += line + "\n"
    return yamlstream    


def get_project_list():
    """
    Loads a yaml file and returns a string of project names, seperated by newlines

    @return project_list (string)
    """
    config_file = ""
    project_list = ""
    try:
        post_yaml = yaml.safe_load(load_raw_yaml_file("config.yaml"))
        config_file = post_yaml["project-path"]
        post_yaml = yaml.safe_load(load_raw_yaml_file(config_file))
        first_item = True 
        for proj in post_yaml:
            if not first_item:
                project_list += "\n"
            else: first_item=False
            project_list += proj["title"]
    except yaml.YAMLError as exc:
        print(exc)
    return project_list


def get_autorun_command(project_name):
    """
    Loads a yaml file and returns a string providing an autorun command, based
    on an input project name

    @param project_name (string)
    @return exc (string) autorun command to execute
    """
    config_file = ""
    default_command = ""
    project_commands = {}
    try:
        # load the config file attributes
        post_yaml = yaml.safe_load(load_raw_yaml_file("config.yaml"))
        config_file = post_yaml["project-path"]
        default_command = post_yaml["default-command"]
        if(project_name == "default_cmd"): return default_command
        for proj in post_yaml["autorun"]:
            new_entry = {}
            new_entry[proj["project"]] = proj["command"]
            project_commands.update(new_entry)
            
        if project_name in project_commands:
            return project_commands[project_name]
        else:
            return default_command
    except yaml.YAMLError as exc:
        print(exc)
   

def main(autorun_project, list_projects=False):
    if list_projects:
        print(get_project_list())
        return
    else:
        print(get_autorun_command(autorun_project))
        return

if __name__ == '__main__':
    # define arguments to parse
    parser = argparse.ArgumentParser(description="Parse Personal Project Yaml Files")
    parser.add_argument('--projects', action='store_true', help='list projects in yaml datafile')
    parser.add_argument('--autorun', type=str, default='default_cmd', nargs='?', help='produce an autorun command based on the project name')

    # send arguments to the main function
    args = parser.parse_args()
    main(args.autorun, args.projects)
    
