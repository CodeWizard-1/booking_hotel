from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic.detail import DetailView
from .models import Room, Guest_reviews, City, Booking, Hotel
from .forms import Guest_reviewsForm, BookingForm, BookingEditForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import BookingForm, BookingEditForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages import success
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class CityListView(View):
    template_name = 'hotel_detail.html',

    def get(self, request):
        cities = City.objects.all()
        context = {'cities': cities}
        return render(request, self.template_name, context)


class HotelList(generic.ListView):
    model = Hotel
    queryset = Hotel.objects.all()
    template_name = 'index.html'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cities'] = City.objects.all()
        context['hotels'] = Hotel.objects.all()
        context['rooms'] = Room.objects.filter(status=1).order_by('-id')
        city = City.objects.get(pk=1)
        context['City'] = city
        return context


class HotelDetail(DetailView):
    model = Hotel
    template_name = 'hotel_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cities'] = City.objects.all()
        context['hotels'] = Hotel.objects.all()
        return context


class CityHotelsView(View):
    template_name = 'city_hotels.html'
    paginate_by = 6

    def get(self, request, city_id):
        city = City.objects.get(pk=city_id)
        hotels = Hotel.objects.filter(city=city)
        cities = City.objects.all()

        paginator = Paginator(hotels, self.paginate_by)
        page = request.GET.get('page')

        try:
            hotels = paginator.page(page)
        except PageNotAnInteger:
            hotels = paginator.page(1)
        except EmptyPage:
            hotels = paginator.page(paginator.num_pages)


        context = {'city': city, 'hotels': hotels, 'cities': cities}
        return render(request, self.template_name, context)


class SearchView(View):
    template_name = 'search.html'

    def post(self, request):
        city_id = request.POST.get('city')

        if city_id:
            return redirect('city_hotels', city_id=city_id)
        else:
            return render(request, self.template_name)

    def get(self, request):
        return render(request, self.template_name)


class RoomList(generic.ListView):
    model = Room
    queryset = Room.objects.filter(status=1).order_by('-id')
    template_name = 'index.html'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        city = City.objects.get(pk=1)
        context['City'] = city
        return context


class RoomDetail(View):
    template_name = "room_detail.html"

    def get(self, request, slug, *args, **kwargs):
        queryset = Room.objects.filter(status=1)
        room = get_object_or_404(queryset, slug=slug)
        reviews = Guest_reviews.objects.filter(
            room=room, approved=True).order_by('-id')
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
        reviews = Guest_reviews.objects.filter(
            room=room, approved=True).order_by('-id')
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


class BookRoomView(View):
    template_name = 'booking.html'

    def get(self, request, slug):
        room = get_object_or_404(Room, slug=slug)
        hotel = room.hotel
        city = hotel.city

        total_price = room.price
        form = BookingForm(initial={'total_price': total_price})

        context = {'room': room, 'city': city, 'hotel': hotel, 'form': form, 'roomId': room.id}

        return render(request, self.template_name, context)

        # return render(request, self.template_name, {'room': room, 'city': city, 'hotel': hotel, 'form': form})

    def post(self, request, slug):
        room = get_object_or_404(Room, slug=slug)
        hotel = room.hotel
        city = hotel.city
        form = BookingForm(request.POST)

        if form.is_valid():
            booking = form.save(commit=False)
            if request.user.is_authenticated:
                booking.customer = request.user
                booking.room = room
                booking.save()
            return redirect('success_booking', booking_id=booking.id)
        else:
            return render(request, self.template_name, {'room': room, 'city': city, 'hotel': hotel, 'form': form})


class BookingDetailView(View):
    template_name = 'my_booking.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        bookings = Booking.objects.filter(customer=user).order_by('-id')
        context = {
            'bookings': bookings,
        }
        
        if not bookings:
            context['no_bookings'] = True

        return render(request, self.template_name, context)

    def post(self, request):
        if 'cancel_booking' in request.POST:
            booking_id = request.POST.get('booking_id')
            booking = get_object_or_404(Booking, id=booking_id)
            if request.user == booking.customer:
                booking.is_cancelled = True
                booking.save()
                return HttpResponseRedirect('/my_booking/')
        return HttpResponseRedirect('/my_booking/')


class CancelBookingView(View):
    def post(self, request, booking_id):
        booking = get_object_or_404(Booking, id=booking_id)
        booking.is_cancelled = True
        booking.save()
        return redirect('my_booking')


class SuccessBookingView(View):
    template_name = "success_booking.html"

    def get(self, request, booking_id, *args, **kwargs):
        booking = get_object_or_404(Booking, id=booking_id)
        total_price = booking.room.price * (booking.checkout_date - booking.checking_date).days
        context = {'booking': booking, 'total_price': total_price}

        return render(request, self.template_name, context)


class EditBookingView(View):
    template_name = 'edit_booking.html'

    def get(self, request, booking_id):
        booking = Booking.objects.get(id=booking_id)
        form = BookingEditForm(instance=booking)
        return render(request, self.template_name, {'form': form, 'booking': booking})

    def post(self, request, booking_id):
        booking = Booking.objects.get(id=booking_id)
        form = BookingEditForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()

            messages.success(request, 'Changes have been successfully saved.')

            return redirect('my_booking')

        total_price = booking.room.price * (booking.checkout_date - booking.checking_date).days

        return render(request, self.template_name, {'form': form, 'booking': booking, 'total_price': total_price})

class RoomLike(View):

    def post(self, request, slug):
        room = get_object_or_404(Room, slug=slug)

        if room.likes.filter(id=request.user.id).exists():
            room.likes.remove(request.user)
        else:
            room.likes.add(request.user)

        return HttpResponseRedirect(reverse('room_detail', args=[slug]))

