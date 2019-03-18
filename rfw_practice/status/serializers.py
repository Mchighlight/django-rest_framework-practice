from rest_framework import serializers


from status.models import Status

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
    class Meta:
        model = Status
        fields = [
            'user',
            'content',
            'image'
        ]

    def validate_content(self, value):
        if len(value) > 1000:
            raise serializers.ValidationError("This is too long")
        return value

    def validate(self, data):
        content = data.get("content", None)
        if content == "":
            content = None
        image = data.get("image", None)
        if content is None and image is None :
            raise serializers.ValidationError("Content or image is required.")
        return data