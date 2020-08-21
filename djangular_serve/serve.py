#!/usr/bin/python3
"""""
DJANGULAR SERVE MAIN
"""""
import os
import shutil
import subprocess

try:
    from djangular_serve.app_settings import STATIC_ROOT, NG_ROOT_PATH
    from djangular_serve.management.utils import Helpers
except NameError:
    from .app_settings import STATIC_ROOT, NG_ROOT_PATH
    from .management.utils import Helpers


class AngularBuild(Helpers):
    """
    Build data
    """
    h = Helpers

    static_path = STATIC_ROOT
    ng_path = NG_ROOT_PATH

    ng_build = "ng build"
    prefix_prod = "--prod --output-path {}".format(static_path)
    prefix_hash = "--output-hashing none"


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
    comp = "{} {} {}".format(ng_build, prefix_prod, prefix_hash)
    print(">> Running", comp, "for {}".format(ng_path))
    command = comp
    os.system(command)

    os.chdir(STATIC_ROOT)

    os.mkdir("ng_js")
    os.mkdir("ng_css")

    js_source = '{}/*.js'.format(STATIC_ROOT)
    js_destination = '{}/{}'.format(STATIC_ROOT, "ng_js")

    css_source = '{}/*.css'.format(STATIC_ROOT)
    css_destination = '{}/{}'.format(STATIC_ROOT, "ng_css")

    os.system("mv {} {}".format(js_source, js_destination))
    os.system("mv {} {}".format(css_source, css_destination))


if __name__ == '__main__':
    ng_deploy()
