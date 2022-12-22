
from django.views.generic import TemplateView
import rest_framework.permissions as perms
import rest_framework.generics as drf_generics
import rest_framework.mixins as drf_mixins
from Jobstler.utils.permissions.IsOwnerOrReadOnly import IsOwnerOrReadOnly
from Jobstler.jobstler_main.models import Advertisement, Comment, UserAccount
from Jobstler.jobstler_main.serializers.common import AdvertisementSerializer, CommentSerializer, UserAccountSerializer


class IndexView(TemplateView):
    template_name = "index.html"


class ReadEditDeleteAdvertisement(drf_mixins.RetrieveModelMixin,
                          drf_mixins.UpdateModelMixin,
                          drf_mixins.DestroyModelMixin,
                          drf_generics.GenericAPIView):

    permission_classes = [perms.IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = AdvertisementSerializer
    queryset = Advertisement.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CreateReadAdvertisements(drf_mixins.ListModelMixin,
                        drf_mixins.CreateModelMixin,
                        drf_generics.GenericAPIView):

    permission_classes = [perms.IsAuthenticated]
    serializer_class = AdvertisementSerializer
    queryset = Advertisement.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user_owner=self.request.user)


class CreateComment(drf_mixins.CreateModelMixin,
                    drf_generics.GenericAPIView):

    permission_classes = [perms.IsAuthenticated]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user_owner=self.request.user)



class ReadEditDeleteComment(drf_mixins.RetrieveModelMixin,
                            drf_mixins.UpdateModelMixin,
                            drf_mixins.DestroyModelMixin,
                            drf_generics.GenericAPIView):

    permission_classes = [perms.IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(self, request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(self, request, *args, **kwargs)


class ReadEditUser(drf_mixins.RetrieveModelMixin,
                        drf_mixins.UpdateModelMixin,
                        drf_generics.GenericAPIView):

    serializer_class = UserAccountSerializer
    permission_classes = [perms.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = UserAccount.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)




