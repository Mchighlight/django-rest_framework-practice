from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from status.models import Status
from .serializers import StatusSerializer


class StatusOneAPIView(
            mixins.CreateModelMixin,
            mixins.RetrieveModelMixin,
            mixins.UpdateModelMixin,
            mixins.DestroyModelMixin,
            generics.ListAPIView
):
    permission_classes = []
    authentication_classes = []
    serializer_class = StatusSerializer

    def get_queryset(self):
        request = self.request
        qs = Status.objects.all()
        query = request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def get_object(self):
        request = self.request
        passed_id = request.GET.get('id')
        queryset = self.get_queryset()
        if passed_id is not None:
            obj = get_object_or_404(queryset, id=passed_id)
            self.check_object_permissions(request, obj)
        return obj

    def get(self, request, *args, **kwargs):
        passed_id = request.GET.get('id')
        if passed_id is not None:
            return self.retrieve(request, *args, **kwargs)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class StatusListSearchAPIView(APIView):
    permission_classes = []
    authentication_classes = []

    def get(self, request, format=None):
        qs = Status.objects.all()
        serializer = StatusSerializer(qs, many=True)
        return Response(serializer.data)

# CreateModelMixin --- post method
# UpdateModelMixin --- put method
# DestroyModelMixin --- delete method


class StatusAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = StatusSerializer

    def get_queryset(self):
        qs = Status.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    # mixins build-in Create function
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # minxins.CreateModelMixin is same as generic.CreateAPIView
    # def perform_create(self, serializer):
    #     serializer.save( user=self.request.user )
  

class StatusCreateAPIView(generics.CreateAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = StatusSerializer
    queryset = Status.objects.all()

    # def perform_create(self, serializer):
    #     serializer.save( user=self.request.user )


# TODO: how to show more detail in seriailzer
class StatusDetailAPIView(mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.RetrieveAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = StatusSerializer
    queryset = Status.objects.all()
    lookup_field = 'id'  # 如果ookup_field沒define的話parmas值要用初始的pk

    # 基本上做的事情和lookup_field依樣
    # def get_object(self, *args, **kwargs):
    #    kwargs = self.kwargs
    #    kw_id = kwargs.get('id')
    #    return Status.objects.get(id=kw_id)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class StatusUpdateAPIView(generics.UpdateAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = StatusSerializer
    queryset = Status.objects.all()
    lookup_field = 'id'


class StatusDeleteAPIView(generics.DestroyAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = StatusSerializer
    queryset = Status.objects.all()
    lookup_field = 'id'

