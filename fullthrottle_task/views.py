# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from fullthrottle_task.models import User, ActivityPeriods


# GET user details with activity Periods API
@api_view(['GET', ])
@permission_classes([IsAuthenticated])
def get_user_details_Api(request):
    if request.user.is_superuser is True:
        users = User.objects.all()
        if request.user.is_superuser is True:
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
        else:
            raise PermissionDenied()



