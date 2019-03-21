from rest_framework import serializers
from status.models import Status
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
        return "/api/status/{id}".format(id=obj.id) 