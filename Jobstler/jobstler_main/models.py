from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from Jobstler.custom_authentication.models import CustomUser

custom_user_model = get_user_model()


class UserAccount(models.Model):
    """
    User model with data for the corresponding user.
    """
    user_owner = models.OneToOneField(custom_user_model, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    is_deleted = models.BooleanField(default=False)


    def __str__(self) -> str:
        """
        Str magic method.
        @return: Returns an interpolated string of the whole User name.
        """
        return f"{self.first_name} {self.middle_name} {self.last_name}"


class Advertisement(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    image_url = models.URLField(max_length=255, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_on = models.DateTimeField()
    is_deleted = models.BooleanField(default=False)
    user_owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class Comment(models.Model):
    advertisement_fk = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    created_on = models.DateTimeField()
    is_deleted = models.BooleanField(default=False)
    text = models.CharField(max_length=500)
    user_owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


