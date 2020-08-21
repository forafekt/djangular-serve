import djangular_serve # noqa
try:
    from djangular_serve.serve import ng_deploy
except NameError:
    from .serve import ng_deploy

ng_deploy()
