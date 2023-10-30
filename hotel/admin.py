from django.contrib import admin
from .models import Room, Hotel, City, Facilities, Category, Booking, Guest_reviews
from django_summernote.admin import SummernoteModelAdmin


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    search_fields = ['city_name',]


@admin.register(Room)
class RoomAdmin(SummernoteModelAdmin):
    list_display = ('hotel', 'room_name', 'slug', 'status', 'is_booked',)
    search_fields = ['room_name', 'description_room']
    prepopulated_fields = {'slug': ('room_name',)}
    list_filter = ('hotel', 'status', 'category', 'price', 'is_booked',)
    summernote_fields = ('description_room',)


@admin.register(Hotel)
class HotelAdmin(SummernoteModelAdmin):
    list_display = ('hotel_name', 'slug',)
    search_fields = ['hotel_name', 'description_hotel']
    prepopulated_fields = {'slug': ('hotel_name',)}
    summernote_fields = ('description_hotel',)


@admin.register(Facilities)
class FacilitiesAdmin(admin.ModelAdmin):
    search_fields = ['name',]


@admin.register(Category)
class FCategoryAdmin(admin.ModelAdmin):
    search_fields = ['category_name',]


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('room', 'booking_date', 'customer',)
    search_fields = ['customer', 'room', 'booking_date',
                     'checking_date', 'checkout_date', 'phone_number', 'email',]
    list_filter = ('customer', 'room', 'booking_date',
                   'checking_date', 'checkout_date', 'phone_number', 'email',)


@admin.register(Guest_reviews)
class Guest_reviewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'room', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_reviews(self, request, queryset):
        queryset.update(approved=True)
