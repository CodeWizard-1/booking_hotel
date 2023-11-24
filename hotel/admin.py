from django.contrib import admin
from .models import Room, Hotel, City, Facilities, Category, Booking, Guest_reviews
from django_summernote.admin import SummernoteModelAdmin
from django.utils import formats


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    search_fields = [
        "city_name",
    ]


@admin.register(Room)
class RoomAdmin(SummernoteModelAdmin):
    list_display = ("hotel", "room_name", "slug", "on_main_display", "status")
    search_fields = ["room_name", "description_room"]
    prepopulated_fields = {"slug": ("room_name",)}
    list_filter = ("hotel", "status", "category", "price")
    summernote_fields = ("description_room",)

    def on_main_display(self, obj):
        return obj.on_main

    on_main_display.boolean = True
    on_main_display.short_description = "Show on Main Page"

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["on_main"].widget.attrs["class"] = "checkbox"
        return form


@admin.register(Hotel)
class HotelAdmin(SummernoteModelAdmin):
    list_display = (
        "hotel_name",
        "on_main_display",
    )
    search_fields = ["hotel_name", "description_hotel"]
    prepopulated_fields = {"slug": ("hotel_name",)}
    summernote_fields = ("description_hotel",)

    def on_main_display(self, obj):
        return obj.on_main

    on_main_display.boolean = True
    on_main_display.short_description = "Show on Main Page"

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["on_main"].widget.attrs["class"] = "checkbox"
        return form


@admin.register(Facilities)
class FacilitiesAdmin(admin.ModelAdmin):
    search_fields = [
        "name",
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = [
        "category_name",
    ]


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "get_hotel",
        "room",
        "booking_date_formatted",
        "checking_date_formatted",
        "checkout_date_formatted",
        "customer",
        "phone_number",
        "child_bed",
        "playroom_services",
        "is_cancelled",
    )
    search_fields = [
        "customer",
        "room",
        "booking_date",
        "checking_date",
        "checkout_date",
        "phone_number",
        "email",
    ]
    list_filter = (
        "customer",
        "room",
        "booking_date",
        "checking_date",
        "checkout_date",
        "phone_number",
        "email",
        "child_bed",
        "playroom_services",
        "is_cancelled",
    )

    def get_hotel(self, obj):
        return obj.room.hotel.hotel_name if obj.room.hotel else None

    get_hotel.short_description = "Hotel"

    def checking_date_formatted(self, obj):
        return formats.date_format(obj.checking_date, "SHORT_DATE_FORMAT")

    checking_date_formatted.short_description = "Checking date"

    def checkout_date_formatted(self, obj):
        return formats.date_format(obj.checkout_date, "SHORT_DATE_FORMAT")

    checkout_date_formatted.short_description = "Checkout date"

    def booking_date_formatted(self, obj):
        return formats.date_format(obj.booking_date, "SHORT_DATETIME_FORMAT")

    booking_date_formatted.short_description = "Booking date"


@admin.register(Guest_reviews)
class Guest_reviewsAdmin(admin.ModelAdmin):
    list_display = ("name", "body", "room", "created_on", "approved")
    list_filter = ("approved", "created_on")
    search_fields = ("name", "email", "body")
    actions = ["approve_comments"]

    def approve_reviews(self, request, queryset):
        queryset.update(approved=True)
