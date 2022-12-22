from rest_framework import serializers

from Jobstler.jobstler_main.models import UserAccount, Comment, Advertisement
from Jobstler.utils.DynamicFieldsSerializer import DynamicFieldsModelSerializer


class UserAccountSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = UserAccount
        exclude = ("is_deleted",)


class CommentSerializer(DynamicFieldsModelSerializer):
    """
    CommentSerializer to get the comment that was exchanged.
    """

    user_owner = serializers.ReadOnlyField(source="user_owner.pk")

    class Meta:
        model = Comment
        exclude = ("is_deleted", )



class AdvertisementSerializer(DynamicFieldsModelSerializer):

    comments = serializers.SerializerMethodField()
    user_owner = serializers.ReadOnlyField(source="user_owner.pk")

    class Meta:
        model = Advertisement
        exclude = ("is_deleted", )

    @staticmethod
    def get_comments(obj):
        comments = Comment.objects.filter(advertisement_fk=obj.pk)
        serializer = CommentSerializer(comments, many=True)
        return serializer.data

    def validate(self, attrs):
        title = attrs.get("title")
        description = attrs.get("description")
        price = attrs.get("price")

        if all([title, description, price]):
            if float(price) < 0:
                raise serializers.ValidationError("Price cannot be lower than zero.")
            return attrs
        else:
            raise serializers.ValidationError("Please fill all fields.")



