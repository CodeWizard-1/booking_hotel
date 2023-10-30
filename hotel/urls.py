from . import views
from django.urls import path


urlpatterns = [
    path('', views.RoomList.as_view(), name='home')
]
