from rest_framework import serializers
from rest_framework.utils.serializer_helpers import ReturnDict

from Jobstler.jobstler_main.models import UserAccount, Comment, Advertisement, Message, PrivateMessageTable
from Jobstler.utils.DynamicFieldsSerializer import DynamicFieldsModelSerializer


class UserAccountSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = UserAccount
        exclude = ("is_deleted", "user")


class CommentSerializer(DynamicFieldsModelSerializer):
    """
    CommentSerializer to get the comment that was exchanged.
    """

    class Meta:
        model = Comment
        exclude = ("is_deleted", )


class AdvertisementSerializer(DynamicFieldsModelSerializer):

    comments = serializers.SerializerMethodField()

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





class MessageSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Message
        exclude = ("is_deleted", )


class PrivateMessageTableSerializer(DynamicFieldsModelSerializer):
    """
    PrivateMessageTableSerializer to get the data for sender, recipient and the message that was sent.
    """
    message = serializers.SerializerMethodField()

    class Meta:
        model = PrivateMessageTable
        fields = "__all__"

    @staticmethod
    def get_message(obj: PrivateMessageTable) -> ReturnDict:
        """
        Gets the message from the private message table's key and the message table.
        @param obj: PrivateMessageTable Object
        @return: Returns OrderedDict as serialized data.
        """
        serializer = MessageSerializer(obj.message)
        return serializer.data

