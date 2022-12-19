from Jobstler.custom_authentication.models import CustomUser
from Jobstler.utils.DynamicFieldsSerializer import DynamicFieldsModelSerializer


class CustomUserSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = CustomUser
        fields = "__all__"