from . import views
from django.urls import path


urlpatterns = [
    path('', views.RoomList.as_view(), name='home'),
    path('<slug:slug>/', views.RoomDetail.as_view(), name='room_detail'),
]
