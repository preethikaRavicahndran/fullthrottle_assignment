# Create your views here.
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from fullthrottle_task.models import User, ActivityPeriods
from fullthrottle_task.serializers import UserSerializer, ActivityPeriodsSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ActivityPeriodsViewSet(viewsets.ModelViewSet):
    queryset = ActivityPeriods.objects.all()
    serializer_class = ActivityPeriodsSerializer


class UserDetailsViewSet(viewsets.ViewSet):

    def list(self, request):
        users = User.objects.all()
        members = []
        for user in users:
            user_data = {}
            user_data["id"] = str(user.id)
            user_data["real_name"] = user.real_name
            user_data["tz"] = user.tz
            activity_periods = ActivityPeriods.objects.filter(user_id=user.id).values('start_time', 'end_time')
            if len(activity_periods) != 0:
                user_data["activity_periods"] = activity_periods
            members.append(user_data)
        context = {"ok": True, "members": members}
        return Response(context, status=status.HTTP_200_OK)


user_list = UserDetailsViewSet.as_view({'get': 'list'})