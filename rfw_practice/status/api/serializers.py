from rest_framework import serializers
from status.models import Status
from rest_framework.reverse import reverse
class StatusInLineUserSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Status
        fields = [
            'id',
            'uri',
            'content',
            'image'
        ]

    def get_uri(self, obj):
        request = self.context.get('request')
        return reverse("api-status:detail", kwargs={'id':obj.id}, request=request)