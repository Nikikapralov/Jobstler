import rest_framework.generics as drf_generics
import rest_framework.mixins as drf_mixins
import rest_framework.permissions as perms
from Jobstler.custom_authentication.models import CustomUser
from Jobstler.jobstler_main.models import Advertisement, Comment, UserAccount
from Jobstler.jobstler_main.serializers.admin_deep import UserSerializerDeepAdmin
from Jobstler.jobstler_main.serializers.common import AdvertisementSerializer, CommentSerializer, UserAccountSerializer


class GetAllUsersAdmin(drf_generics.ListAPIView):
    permission_classes = [perms.IsAdminUser]
    serializer_class = UserSerializerDeepAdmin
    queryset = CustomUser.objects.all()


class ReadEditUserAdmin(drf_mixins.RetrieveModelMixin,
                        drf_mixins.UpdateModelMixin,
                        drf_generics.GenericAPIView):

    serializer_class = UserAccountSerializer
    permission_classes = [perms.IsAdminUser]
    queryset = UserAccount.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class ReadEditDeleteAdvertisementAdmin(drf_mixins.RetrieveModelMixin,
                              drf_mixins.UpdateModelMixin,
                              drf_mixins.DestroyModelMixin,
                              drf_generics.GenericAPIView):

    serializer_class = AdvertisementSerializer
    permission_classes = [perms.IsAdminUser]
    queryset = Advertisement.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ReadEditDeleteCommentAdmin(drf_mixins.RetrieveModelMixin,
                              drf_mixins.UpdateModelMixin,
                              drf_mixins.DestroyModelMixin,
                              drf_generics.GenericAPIView):

    serializer_class = CommentSerializer
    permission_classes = [perms.IsAdminUser]
    queryset = Comment.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


