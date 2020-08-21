from django.conf.urls import url

from .views import manifest, service_worker, offline, serve_funnel
from .app_settings import SERVICE_WORKER_NAME
urlpatterns = [
    url('^$', serve_funnel, name='serve'),
    url('^{}$'.format(SERVICE_WORKER_NAME), service_worker, name='serviceworker'),
    url('^manifest.json$', manifest, name='manifest'),
    url('^offline/$', offline, name='offline'),
]
