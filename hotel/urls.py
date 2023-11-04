from . import views
from django.urls import path
from .views import EditBookingView


urlpatterns = [
    path('', views.RoomList.as_view(), name='home'),
    path('success-booking/', views.SuccessBookingView.as_view(),
         name='success_booking'),
    path('my_booking/', views.BookingDetailView.as_view(), name='my_booking'),
    path('cancel_booking/<int:booking_id>/',
         views.BookingDetailView.as_view(), name='cancel_booking'),
    path('edit_booking/<int:booking_id>/',
         EditBookingView.as_view(), name='edit_booking'),
    path('<slug:slug>/', views.RoomDetail.as_view(), name='room_detail'),
    path('<slug:slug>/booking/', views.BookRoomView.as_view(), name='book_room'),
]
