#!/usr/bin/python3
"""""
DJANGULAR SERVE MAIN
IN DEVELOPMENT
"""""
import os
import re

try:
    from djangular_serve.management.utils import Helpers
    from djangular_serve.management.handlers import get_img_extension, _mv, get_project_static_root, get_ng_root_path
except NameError:
    from .management.utils import Helpers
    from .management.handlers import get_img_extension, _mv, get_project_static_root, get_ng_root_path


class AngularBuild:
    """
    Build data
    """

    static_path = get_project_static_root()
    ng_path = get_ng_root_path()

    ng_build = "ng build"
    prefix_prod = "--prod --output-path {}".format(static_path)
    prefix_hash = "--output-hashing none"


class OutputDestination(AngularBuild):
    """
    Gather destination for static
    """
    b = AngularBuild
    static_url = b.static_path

    js_source = '{}/*.js'.format(static_url)
    js_path_input = os.path.join(static_url, input(">> JS DIRNAME: "))
    js_destination = '{}/{}'.format(static_url, _mv(files=js_source, dest=js_path_input))
    print(js_path_input)

    css_source = '{}/*.css'.format(static_url)
    css_path_input = os.path.join(static_url, input(">> CSS DIRNAME: "))
    css_destination = '{}/{}'.format(static_url, _mv(files=css_source, dest=css_path_input))
    print(css_path_input)

    types = r'*.ico *.jpg *.jpeg *.png *.gif *.svg'
    file_extensions = re.findall(r'[\w\.-]+.[\w\.-]+', types.strip())
    for fe in file_extensions:
        img_source = '{}/{}'.format(static_url, types)
        img_path_input = os.path.join(static_url, input(">> IMAGE DIRNAME: "))
        img_destination = '{}/{}'.format(static_url, _mv(files=img_source, dest=img_path_input))
        exit(img_source)

    def __init__(self):
        self.js_output = _mv(self.js_source, self.js_destination)
        self.css_output = _mv(self.css_source, self.css_destination)
        self.img_output = _mv(self.img_source, self.img_destination)


def ng_deploy():
    """
    Build Angular project to Django static and organise.
    """
    b = AngularBuild()

    ng_build = b.ng_build  # ng build
    prefix_prod = b.prefix_prod  # --prod --output-path ./../../
    prefix_hash = b.prefix_hash  # --output-hashing none
    ng_path = b.ng_path  # Path where Angular project is

    os.chdir(ng_path)  # Automatically get Angular project without CD

    # Gather data and execute command
    compile_ = "{} {} {}".format(ng_build, prefix_prod, prefix_hash)
    print(">> Running", compile_, "for {}".format(ng_path))
    command = compile_
    process = os.system(command)
    return process


def static_dirs_manager():
    """
    Prompt manager to ask if user wants to move files to subdirectories.
    For example: mv *.js to js folder and / or *.css to css folder.
    """
    print("Do you want to move files to subdirs? Y/n")
    io = OutputDestination

    return io


if __name__ == '__main__':
    ng_deploy()
    static_dirs_manager()
