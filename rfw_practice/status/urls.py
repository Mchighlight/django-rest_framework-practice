from django.urls import path
from status import views

urlpatterns = [
    #path('search/', views.StatusListSearchAPIView.as_view(), name='search_list'),
    #path('', views.StatusAPIView.as_view(), name='search'),
    #path('create/', views.StatusCreateAPIView.as_view(), name='create'),
    path('<int:id>/', views.StatusAPIDetailView.as_view(), name='detail'),
    #path('<int:id>/update/', views.StatusUpdateAPIView.as_view(), name='update'),
    #path('<int:id>/delete/', views.StatusDeleteAPIView.as_view(), name='delete'),
    path('', views.StatusOneAPIView.as_view(), name='one_end_point')
]

