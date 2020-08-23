import djangular_serve # noqa
try:
    from djangular_serve.serve import ng_deploy, static_dirs_manager
except NameError:
    from .serve import ng_deploy, static_dirs_manager

ng_deploy()
static_dirs_manager()
