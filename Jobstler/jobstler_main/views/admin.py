import rest_framework.generics as drf
import rest_framework.permissions as perms
from django.http import Http404

from Jobstler.custom_authentication.models import CustomUser
from Jobstler.jobstler_main.serializers.admin_deep import UserSerializerDeepAdmin


class GetAllUsersAdmin(drf.ListAPIView):
    permission_classes = []
    serializer_class = UserSerializerDeepAdmin
    queryset = CustomUser.objects.all()