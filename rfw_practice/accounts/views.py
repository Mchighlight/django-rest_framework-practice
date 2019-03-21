from django.contrib.auth import authenticate, get_user_model
from django.db.models import Q
from rest_framework import permissions, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
from .permissions import AnonPermissionOnly

from .serializers import UserRegisterSerializer
from .api.utils import jwt_response_payload_handler

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

User = get_user_model()

class AuthView(APIView):
    permission_classes = [AnonPermissionOnly]
    def post(self, request, *args, **kwargs):
        print(request.user)
        #if request.user.is_authenticated:
        #    return Response({'detail':'YOu are already autehntiacted'}, status=400)
        data = request.data
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        qs = User.objects.filter(
            Q(username__iexact=username)|
            Q(email__iexact=username)
        )
        if qs.count() > 0:
            user_obj = qs.first()
            if user_obj.check_password(password):
                user = user_obj                
                payload = jwt_payload_handler(user)
                token = jwt_encode_handler(payload)
                response = jwt_response_payload_handler(token, user, request=self.request)
                return Response(response)
        return Response({'detail':'Invalid credentials'}, status=401)

class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_class = [AnonPermissionOnly]


    def get_serializer_context(self, *args, **kwargs):
        return {"request":self.request}

'''
class RegisterAPIView(APIView):
    permission_classes = []
    def post(self, request, *args, **kwargs):
        print(request.user)
        if request.user.is_authenticated:
            return Response({'detail':'YOu are already autehntiacted and are register'}, status=400)
        data = request.data
        username = data.get('username')
        email    = data.get('username')
        password = data.get('password')
        password2 = data.get('password2')

        qs = User.objects.filter(
            Q(username__iexact=username)|
            Q(email__iexact=username)
        )
        if password != password2:
            return Response({"detail": "Pssword must math"}, status=401)
        if qs.exist():
            return Response({"detail": "This user already exist"}, status=401)
        else :
            user = User.objects.create(username=username, email=email)
            user.set_password(password)
            user.save()
            return Response({'detail':"Create user successful"}, status=201)
        return Response({'detail':'Invalid credentials'}, status=401)
'''