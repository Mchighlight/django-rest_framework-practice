import datetime
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.conf import settings
from django.utils import timezone
from .api.utils import jwt_response_payload_handler
expire_delta = settings.JWT_AUTH['JWT_REFRESH_EXPIRATION_DELTA']

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

User = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style ={'input_type':'password'}, write_only=True)
    password2 = serializers.CharField(style ={'input_type':'password'}, write_only=True)
    token = serializers.SerializerMethodField(read_only=True)
    expires = serializers.SerializerMethodField(read_only=True)
    token_response = serializers.SerializerMethodField(read_only=True)
    # write_only : don't show the field
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'password2',
            'token',
            'expires',
            'token_response'
        ]
        extra_kwargs = {'password':{'write_only':True}}

    def validate_email(self, value):
        qs = User.objects.filter(email__iexact=value)
        if qs.exists():
            raise serializers.ValidationError("User with this email already exists")
        return value
    
    def validate_user(self, value):
        qs = User.objects.filter(usernam__iexact=value)
        if qs.exists():
            raise serializers.ValidationError("User with this username already exists")
        return value    

    def validate(self, attrs):
        pw = attrs.get('password')
        pw2 = attrs.pop('password2')
        if pw != pw2 :
            raise serializers.ValidationError("passwords must match")
        return attrs

    def get_token(self, obj): 
        user = obj                
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return token

    def get_expires(self, obj): 
        return timezone.now() + expire_delta - datetime.timedelta(seconds=200)

    def get_token_response(self, obj): 
        user = obj 
        context = self.context               
        response = jwt_response_payload_handler(self.get_token(obj), user, request=context['request'])
        return response 

    def create(self, validate_data):
        user_obj = User(
            username = validate_data.get("username"),
            email = validate_data.get("email")
        )
        user_obj.set_password(validate_data.get('password'))
        user_obj.is_active = False
        user_obj.save()
        return user_obj