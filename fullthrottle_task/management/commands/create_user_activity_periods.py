from django.core.management.base import BaseCommand
from fullthrottle_task.models import User, ActivityPeriods
import random
from datetime import datetime


class Command(BaseCommand):
    help = 'Create activity periods for user'

    def add_arguments(self, parser):
        parser.add_argument('id', type=str)
        parser.add_argument('start_time', type=str)
        parser.add_argument('end_time', type=str)

    def handle(self, *args, **options):
        ActivityPeriods.objects.create(user_id=options["id"], start_time=options["start_time"], end_time=options["end_time"])

        self.stdout.write(self.style.SUCCESS('Successfully created activity Periods for user'))