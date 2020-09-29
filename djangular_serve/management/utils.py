import os
from pathlib import Path # noqa

from djangular_serve import app_settings


class Helpers(object):
    """
    Mixin to get commonly used directories in Djangular Commands
    """

    """ 
    Get static root to build angular out to django. 
    """

    def get_ng_root_path(self):
        """
        Angular project root path.
        :return:
        """
        return getattr(app_settings, 'NG_ROOT_PATH', ".")

    def get_project_static_root(self):
        """
        Find django static root
        """
        static_path = getattr(app_settings, "STATIC_ROOT", ".")
        return static_path
