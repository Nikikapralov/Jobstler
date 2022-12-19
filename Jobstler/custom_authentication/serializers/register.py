from django.contrib.auth import authenticate

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from Jobstler.custom_authentication.validators import validate_over_LIMIT_AGE


class RegisterSerializer(serializers.Serializer):
    email = serializers.CharField(label="email", write_only=True)
    password = serializers.CharField(label="password", write_only=True, trim_whitespace=False)
    conf_password = serializers.CharField(label="conf_password", write_only=True, trim_whitespace=False)
    date_of_birth = serializers.DateField(label="date_of_birth")

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")
        conf_password = attrs.get("conf_password")
        date_of_birth = attrs.get("date_of_birth")

        if email and password and conf_password and date_of_birth:
            if password != conf_password:
                message = "Password and confirm password do not match."
                raise serializers.ValidationError(message, code="authorization")

            try:
                validate_over_LIMIT_AGE(date_of_birth)
            except ValidationError as error:
                message = error.detail
                raise serializers.ValidationError(message, code="authorization")

        else:
            message = 'Please enter the required data in order to register. One of the fields was empty.'
            raise serializers.ValidationError(message, code="authorization")

        return attrs
