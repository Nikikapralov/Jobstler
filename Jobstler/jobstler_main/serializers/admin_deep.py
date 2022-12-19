from rest_framework import serializers
from rest_framework.utils.serializer_helpers import ReturnList

from Jobstler.custom_authentication.models import CustomUser
from Jobstler.jobstler_main.models import Advertisement, UserAccount
from Jobstler.jobstler_main.serializers.common import UserAccountSerializer, AdvertisementSerializer
from Jobstler.utils.DynamicFieldsSerializer import DynamicFieldsModelSerializer


class UserSerializerDeepAdmin(DynamicFieldsModelSerializer):
    account_data = serializers.SerializerMethodField()
    advertisements = serializers.SerializerMethodField()


    class Meta:
        model = CustomUser
        exclude = ("is_staff", "is_superuser", "password", "groups", "user_permissions")

    @staticmethod
    def get_account_data(obj: CustomUser) -> ReturnList:
        account_data = UserAccount.objects.filter(user=obj.pk)
        serializer = UserAccountSerializer(account_data, many=False)
        return serializer.data

    @staticmethod
    def get_advertisements(obj: CustomUser) -> ReturnList:
        account_data = UserAccount.objects.get(user=obj.pk)
        advertisements = Advertisement.objects.filter(user_owner=account_data)
        serializer = AdvertisementSerializer(advertisements, many=True)
        return serializer.data



