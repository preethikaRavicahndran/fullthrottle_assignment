from rest_framework import serializers
from fullthrottle_task.models import User, ActivityPeriods


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'real_name', 'tz',)


class ActivityPeriodsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ActivityPeriods
        fields = ('user_id', 'start_time', 'end_time',)