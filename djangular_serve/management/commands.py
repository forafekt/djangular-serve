from django.core.management.base import BaseCommand
from djangular_serve.serve import ng_deploy


class Command(BaseCommand):
    help = 'Run ng build'

    def handle(self, *args, **options):
        ng_deploy()
