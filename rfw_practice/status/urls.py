from django.urls import path
from .views import StatusListSearchAPIView, StatusSearchAPIView

urlpatterns = [
    path('', StatusListSearchAPIView.as_view(), name='search_list'),
    path('/search/', StatusSearchAPIView.as_view(), name='search'),
    #path('create/', StatusCreateAPIView.as_view(), name='create'),
    #path('<int:id>/', StatusDetailAPIView.as_view(), name='detail'),
    #path('<int:id>/update/', StatusUpdateAPIView.as_view(), name='update'),
    #path('<int:id>/delete/', StatusDeleteAPIView.as_view(), name='delete'),
]

