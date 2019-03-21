from rest_framework import serializers
from rest_framework.reverse import reverse
#from accounts.serializers import UserPublicSerializer
from status.models import Status
from accounts.user.serializers import  UserPublicSerializer

### Retrieve
'''
obj = Status.objects.first()
data = StatuSerializer(obj)
From rest_framwork.rednerers import JSONRenderer
js = JSONRenderers().render(data.data)
json.load(js)

qs = Status.objects.all()
serizlier = StatusSerizliers(qs, many=True)
jss= JSONRenderer().render(serizlier.data)
json.load(jss)
'''
### Create
'''
data = {'user':1}
serializer = StatusSerizlier(data=data)
if  serializer.is_valid()
    serializer.save()
'''  
### Update
'''
obj = Status.objects.first()
data ={'content':'some new content' }
update_serizlizer = Statusserializer(obj, data= data)
if update_serializer.is_valid()
    update_serializer.save()
'''
### Delete
'''
data ={'user':1, 'content':'some new content' }
create_obj_serial = StatusSerializer(data=data)
create_obj = create_obj_serial.save()

obj = Status.objects.last()
get_data_serializer = StatusSerizlier(obj)
print(obj.delete())
'''
'''
class CustomSerializer(serializers.Serializer):
    content = serializers.CharField()
'''

# 沒有save function


  

class StatusSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    user =   UserPublicSerializer(read_only=True)
    #user_id = serializers.PrimaryKeyRelatedField(read_only=True, source='user')
    #user = serializers.SlugRelatedField( read_only=True, slug_field='email')
    class Meta:
        model = Status
        fields = [
            'user_id',
            'user',
            'uri',
            'content',
            'image'
        ]
        read_only_fields = ['user'] # GET

    def get_uri(self, obj):
        # add domain address
        request = self.context.get('request')
        user = obj.user
        return UserPublicSerializer(user, read_only=True, context={"request": request}).data

    def get_uri(self, obj):
                # add domain address
        request = self.context.get('request')
        return reverse("api-status:detail", kwargs={'id':obj.id}, request=request)

    def validate_content(self, value):
        if len(value) > 1000:
            raise serializers.ValidationError("This is too long")
        return value

    def validate(self, data):
        content = data.get("content", None)
        if content == "":
            content = None
        image = data.get("image", None)
        if content is None and image is None:
            raise serializers.ValidationError("Content or image is required.")
        return data
