from . import views
from django.urls import path


urlpatterns = [
    path('', views.RoomList.as_view(), name='home'),
    path('success-booking/', views.SuccessBookingView.as_view(),
         name='success_booking'),
    path('my_booking/', views.BookingDetailView.as_view(), name='my_booking'),
    path('<slug:slug>/', views.RoomDetail.as_view(), name='room_detail'),
    path('<slug:slug>/booking/', views.BookRoomView.as_view(), name='book_room'),
    
]
