from django.core.management.base import BaseCommand
from crs.models import crs

class Command(BaseCommand):
    def handle(self, *args, **options):
        crs.objects.all().delete()

