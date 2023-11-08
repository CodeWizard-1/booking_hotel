from . import views
from django.urls import path
from .views import EditBookingView, SuccessBookingView, CityListView


urlpatterns = [
    # path('', views.RoomList.as_view(), name='home'),
    path('', views.HotelList.as_view(), name='home'),
    path('success-booking/<int:booking_id>/',
         SuccessBookingView.as_view(), name='success_booking'),
    path('success-booking/', views.SuccessBookingView.as_view(),
         name='success_booking_default'),
    path('my_booking/', views.BookingDetailView.as_view(), name='my_booking'),
    path('cancel_booking/<int:booking_id>/',
         views.BookingDetailView.as_view(), name='cancel_booking'),
    path('edit_booking/<int:booking_id>/',
         EditBookingView.as_view(), name='edit_booking'),
    path('hotel/<slug:slug>/', views.HotelDetail.as_view(), name='hotel_detail'),
    path('room/<slug:slug>/', views.RoomDetail.as_view(), name='room_detail'),
    path('<slug:slug>/booking/',
         views.BookRoomView.as_view(), name='book_room'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('city/<int:city_id>/', views.CityHotelsView.as_view(), name='city_hotels'),
]
