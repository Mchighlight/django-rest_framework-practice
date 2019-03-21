from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.reverse import reverse
from status.api.serializers import StatusInLineUserSerializer

User = get_user_model()

class UserDetailSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    status = serializers.SerializerMethodField(read_only=True)
    statues = StatusInLineUserSerializer(source='status_set', many=True, read_only=True)
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'uri',
            'status',
            'statues'
        ]
    def get_uri(self, obj):
        # add domain addrres
        request = self.context.get('request')
        return reverse("api-user:detail", kwargs={'username':obj.username}, request=request)

    def get_status(self, obj):
        request = self.context.get('request')
        limit = 10
        if request:
            limit_query = request.GET.get('limit')
            try:
                limit = int(limit_query)
            except:
                pass
        qs = obj.status_set.all().order_by("-timestamp")
        data = {
            'uri': self.get_uri(obj) + "status/",
            'last': StatusInLineUserSerializer(qs.first()).data,
            'recent': StatusInLineUserSerializer(qs[:limit], many=True).data
        }
        return data

class UserPublicSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'uri'
        ]
    
    def get_uri(self, obj):
        request = self.context.get('request')
        return reverse("api-user:detail", kwargs={'username':obj.username}, request=request)