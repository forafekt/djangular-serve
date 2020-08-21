from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ServeConfig(AppConfig):
    """""
    Djangular Serve AppConfig
    """""
    name = 'djangular_serve'
    verbose_name = _('Djangular Serve')
