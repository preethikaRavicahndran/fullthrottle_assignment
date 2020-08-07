from django.core.management.base import BaseCommand
from fullthrottle_task.models import User


class Command(BaseCommand):
    help = 'Create users'

    def add_arguments(self, parser):
        parser.add_argument('real_name', type=str)
        parser.add_argument('tz', type=str)

    def handle(self, *args, **options):
        User.objects.create(real_name=options["real_name"], tz=options["tz"])

        self.stdout.write(self.style.SUCCESS('Successfully created users'))