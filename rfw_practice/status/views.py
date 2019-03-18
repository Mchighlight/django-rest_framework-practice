from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.response import Response

from status.models import Status
from .serializers import StatusSerializer
'''
urlpatterns = [
    path('', StatusListSearchAPIView.as_view(), name='search'),
    path('create/', StatusCreateAPIView.as_view(), name='create'),
    path('<int:id>/', StatusDetailAPIView.as_view(), name='detail'),
    path('<int:id>/update/', StatusUpdateAPIView.as_view(), name='update'),
    path('<int:id>/delete/', StatusDeleteAPIView.as_view(), name='delete'),
]
'''


# what is APIView
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