from rest_framework.permissions import BasePermission

from datetime import timedelta
from  django.utils import timezone

class IsOwner(BasePermission):
    message = "You must be the user of this booking or admin."

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or (obj.user == request.user):
            return True
        else:
            return False

class Is3Days(BasePermission):
    message = "it must be 3 days old or less"
    def has_object_permission(self, request, view, obj):
        start_date = obj.date
        end_date = timezone.now().date() + timedelta( days=3 ) 
        if obj.date > end_date:
            return True
        else:
            return False

