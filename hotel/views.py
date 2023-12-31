from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic.detail import DetailView
from .models import Room, Guest_reviews, City, Booking, Hotel
from .forms import Guest_reviewsForm, BookingForm, BookingEditForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages import success
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime, timedelta, date
from django.http import Http404
from django.http import HttpResponse, HttpResponseNotFound

# View for displaying the list of cities
class CityListView(View):
    template_name = ("hotel_detail.html",)

    def get(self, request):
        cities = City.objects.all()
        context = {"cities": cities}
        return render(request, self.template_name, context)


# View for displaying the list of hotels
class HotelList(generic.ListView):
    model = Hotel
    template_name = "index.html"
    ordering = "hotel_name"
    context_object_name = "hotels"

    def get_queryset(self):
        return Hotel.objects.filter(on_main=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cities"] = City.objects.all()
        context["rooms"] = Room.objects.filter(status=1).order_by("-id")

        city_id = self.request.GET.get("city_id")
        context["City"] = City.objects.get(pk=city_id) if city_id else None

        return context

# View for displaying the details of a hotel
class HotelDetail(DetailView):
    model = Hotel
    template_name = "hotel_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cities"] = City.objects.all()
        context["hotels"] = Hotel.objects.all()
        return context

# View for displaying hotels in a specific city
class CityHotelsView(View):
    template_name = "city_hotels.html"
    paginate_by = 4

    def get(self, request, city_id):
        city = City.objects.get(pk=city_id)
        hotels = Hotel.objects.filter(city=city)
        cities = City.objects.all()

        paginator = Paginator(hotels, self.paginate_by)
        page = request.GET.get("page")

        try:
            hotels = paginator.page(page)
        except PageNotAnInteger:
            hotels = paginator.page(1)
        except EmptyPage:
            hotels = paginator.page(paginator.num_pages)

        context = {"city": city, "hotels": hotels, "cities": cities}
        return render(request, self.template_name, context)

 # View for handling search functionality
class SearchView(View):
    template_name = "search.html"

    def post(self, request):
        city_id = request.POST.get("city")

        if city_id:
            return redirect("city_hotels", city_id=city_id)
        else:
            return render(request, self.template_name)

    def get(self, request):
        return render(request, self.template_name)

# View for displaying the list of rooms
class RoomList(generic.ListView):
    model = Room
    queryset = Room.objects.filter(status=1).order_by("-id")
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        city = City.objects.get(pk=1)
        context["City"] = city
        return context

# View for displaying the details of a room
class RoomDetail(View):
    template_name = "room_detail.html"

    def get(self, request, slug, *args, **kwargs):
        queryset = Room.objects.filter(status=1)
        room = get_object_or_404(queryset, slug=slug)
        reviews = Guest_reviews.objects.filter(room=room, approved=True).order_by("-id")
        liked = False

        if request.user.is_authenticated:
            if room.likes.filter(id=request.user.id).exists():
                liked = True

        cities = City.objects.all()

        context = {
            "room": room,
            "reviews": reviews,
            "liked": liked,
            "commented": False,
            "reviews_form": Guest_reviewsForm(),
            "cities": cities,
        }

        return render(request, self.template_name, context)

    def post(self, request, slug, *args, **kwargs):
        queryset = Room.objects.filter(status=1)
        room = get_object_or_404(queryset, slug=slug)
        reviews = Guest_reviews.objects.filter(room=room, approved=True).order_by("-id")
        liked = False

        if request.user.is_authenticated:
            if room.likes.filter(id=request.user.id).exists():
                liked = True

        reviews_form = Guest_reviewsForm(data=request.POST)

        if reviews_form.is_valid():
            reviews_form.instance.email = request.user.email
            reviews_form.instance.name = request.user.username
            new_review = reviews_form.save(commit=False)
            new_review.room = room
            new_review.save()
        else:
            reviews_form = Guest_reviewsForm()

        cities = City.objects.all()

        context = {
            "room": room,
            "reviews": reviews,
            "commented": True,
            "liked": liked,
            "reviews_form": reviews_form,
            "cities": cities,
        }

        return render(request, self.template_name, context)

# View for handling room booking
class BookRoomView(View):
    template_name = "booking.html"

    def get(self, request, slug):
        room = get_object_or_404(Room, slug=slug)
        hotel = room.hotel
        city = hotel.city


        total_price = room.price
        form = BookingForm(
            request=request, room=room, initial={"total_price": total_price}
        )

        bookings = Booking.objects.filter(room=room)
        booked_dates = []
        if bookings.exists():
            for booking in bookings:
                if booking.is_cancelled:
                    continue
                if booking.checking_date and booking.checkout_date:
                    current_date = booking.checking_date
                    while current_date <= booking.checkout_date: 
                        booked_dates.append(current_date.strftime("%Y-%m-%d"))
                        current_date += timedelta(days=1)

 
        context = {
            "room": room,
            "city": city,
            "hotel": hotel,
            "form": form,
            "booked_dates": booked_dates,
        }

        return render(request, self.template_name, context)

    def post(self, request, slug):
        room = get_object_or_404(Room, slug=slug)
        hotel = room.hotel
        city = hotel.city
        form = BookingForm(request.POST, request=request, room=room)

        if form.is_valid():
            if request.user.is_authenticated:
                booking = form.save(commit=False)
                booking.customer = request.user
                booking.room = room
                booking.save()
                return redirect("success_booking", booking_id=booking.id)
        else:
            return render(
                request,
                self.template_name,
                {"room": room, "city": city, "hotel": hotel, "form": form},
            )

# View for displaying user's booking details
class BookingDetailView(View):
    template_name = "my_booking.html"

    def get(self, request, *args, **kwargs):
        user = request.user
        bookings = Booking.objects.filter(customer=user).order_by(
            "-is_cancelled", "-id"
        )
        active_bookings = [booking for booking in bookings if not booking.is_cancelled]
        cancelled_bookings = [booking for booking in bookings if booking.is_cancelled]

        sorted_bookings = active_bookings + cancelled_bookings

        context = {
            "bookings": sorted_bookings,
        }

        if not bookings:
            context["no_bookings"] = True

        return render(request, self.template_name, context)

    def post(self, request):
        if "cancel_booking" in request.POST:
            booking_id = request.POST.get("booking_id")
            booking = get_object_or_404(Booking, id=booking_id)
            if request.user == booking.customer:
                booking.is_cancelled = True
                booking.save()

                return HttpResponseRedirect("/my_booking/")
        return HttpResponseRedirect("/my_booking/")

# View for handling cancellation of a booking
class CancelBookingView(View):
    def post(self, request, booking_id):
        booking = get_object_or_404(Booking, id=booking_id)
        booking.is_cancelled = True
        booking.save()
        messages.success(request, "Booking was successfully canceled!")
        return redirect("my_booking")

# View for displaying a success message after booking
class SuccessBookingView(View):
    template_name = "success_booking.html"

    def get(self, request, booking_id, *args, **kwargs):
        booking = get_object_or_404(Booking, id=booking_id)
        total_price = (
            booking.room.price * (booking.checkout_date - booking.checking_date).days
        )
        context = {"booking": booking, "total_price": total_price}

        return render(request, self.template_name, context)

 # View for editing a booking
class EditBookingView(View):
    template_name = "edit_booking.html"


    def get(self, request, booking_id):

        booking = get_object_or_404(Booking, id=booking_id)


        form = BookingEditForm(instance=booking)
        room = booking.room

        other_bookings = Booking.objects.filter(room=room).exclude(id=booking.id)
        booked_dates = []
        for other_booking in other_bookings:
            if other_booking.is_cancelled:
                continue 
            current_date = other_booking.checking_date
            while current_date <= other_booking.checkout_date:
                booked_dates.append(current_date.strftime("%Y-%m-%d"))
                current_date += timedelta(days=1)


        form.fields['checking_date'].initial = booking.checking_date
        form.fields['checkout_date'].initial = booking.checkout_date

        return render(
            request,
            self.template_name,
            {"form": form, "booking": booking, "booked_dates": booked_dates},
        )

    def post(self, request, booking_id):
        booking = Booking.objects.get(id=booking_id)

        

        form = BookingEditForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()

            messages.success(request, "Changes have been successfully saved!")

            return redirect("my_booking")

        total_price = (
            booking.room.price * (booking.checkout_date - booking.checking_date).days
        )

        booked_dates = (
            Booking.objects.filter(room=booking.room)
            .exclude(id=booking.id)
            .values_list("checking_date", "checkout_date")
        )
        booked_dates = [str(date) for dates in booked_dates for date in dates]

        return render(
            request,
            self.template_name,
            {
                "form": form,
                "booking": booking,
                "total_price": total_price,
                "booked_dates": booked_dates,
            },
        )

# View for handling room likes
class RoomLike(View):
    def post(self, request, slug):
        room = get_object_or_404(Room, slug=slug)

        if room.likes.filter(id=request.user.id).exists():
            room.likes.remove(request.user)
        else:
            room.likes.add(request.user)

        return HttpResponseRedirect(reverse("room_detail", args=[slug]))

# View for handling 404 errors
def custom_page_not_found(request, exception):
    return render(request, '404.html', status=404)


def custom_server_error(request):
    return render(request, '404.html', status=500)