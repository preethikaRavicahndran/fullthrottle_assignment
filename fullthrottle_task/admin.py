from django.contrib import admin
from fullthrottle_task.models import User, ActivityPeriods

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'real_name', 'tz')


class ActivityPeriodsAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'start_time', 'end_time')


admin.site.register(User, UserAdmin)
admin.site.register(ActivityPeriods, ActivityPeriodsAdmin)
