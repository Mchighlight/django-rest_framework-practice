from rest_framework.views import APIView
from rest_framework import generics
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


class StatusAPIView(generics.ListAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = StatusSerializer

    def get_queryset(self):
        qs = Status.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    
class StatusCreateAPIView(generics.CreateAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = StatusSerializer
    queryset = Status.objects.all()

    # def perform_create(self, serializer):
    #     serializer.save( user=self.request.user )


class StatusDetailAPIView(generics.RetrieveAPIView):
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