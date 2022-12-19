from django.urls import path

from Jobstler.jobstler_main.views.admin import GetAllUsersAdmin
from Jobstler.jobstler_main.views.normal import IndexView, \
    CreateComment, ReadEditDeleteComment, CreateReadAdvertisements, ReadEditDeleteAdvertisement, CreateReadMessages, \
    ReadEditDeleteMessage

urlpatterns = [
    path("", IndexView.as_view()),
    path("advertisements/", CreateReadAdvertisements.as_view()),
    path("advertisements/<int:pk>", ReadEditDeleteAdvertisement.as_view()),
    path("advertisements/comment", CreateComment.as_view()),
    path("advertisemnets/comment/<int:pk>", ReadEditDeleteComment.as_view()),
    path("message/", CreateReadMessages.as_view()),
    path("message/<int:pk>", ReadEditDeleteMessage.as_view()),
    path("administration/users/", GetAllUsersAdmin.as_view()),
    path("administration/advertisements/<int:pk>", ReadEditDeleteAdvertisementAdmin.as_view()),
    path("administration/comment/<int:pk>", ReadEditDeleteCommentAdmin.as_view()),
    path("administration/message/<int:pk>", ReadDeleteMessageAdmin.as_view()),
]