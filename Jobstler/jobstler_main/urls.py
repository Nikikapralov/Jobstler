from django.urls import path

from Jobstler.jobstler_main.views.admin import GetAllUsersAdmin, ReadEditDeleteAdvertisementAdmin, \
    ReadEditDeleteCommentAdmin
from Jobstler.jobstler_main.views.normal import IndexView, \
    CreateComment, ReadEditDeleteComment, CreateReadAdvertisements, ReadEditDeleteAdvertisement

urlpatterns = [
    path("", IndexView.as_view()),
    path("advertisements/", CreateReadAdvertisements.as_view()),
    path("advertisements/<int:pk>/", ReadEditDeleteAdvertisement.as_view()),
    path("advertisements/comment/", CreateComment.as_view()),
    path("advertisemnets/comment/<int:pk>/", ReadEditDeleteComment.as_view()),
    path("administration/users/", GetAllUsersAdmin.as_view()),
    path("administration/advertisements/<int:pk>/", ReadEditDeleteAdvertisementAdmin.as_view()),
    path("administration/comment/<int:pk>/", ReadEditDeleteCommentAdmin.as_view()),
]