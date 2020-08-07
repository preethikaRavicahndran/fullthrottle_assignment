import uuid

from django.db import models

# Create your models here.
from fullthrottle_task.managers import UserManager


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    real_name = models.CharField(max_length=150)
    tz = models.CharField(max_length=150)

    objects = UserManager()


class ActivityPeriods(models.Model):
    user_id = models.CharField(max_length=150)
    start_time = models.CharField(max_length=150)
    end_time = models.CharField(max_length=150)
