from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from .models import Room, Guest_reviews, City, Booking
from .forms import Guest_reviewsForm, BookingForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import BookingForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


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

        context = {
            "room": room,
            "reviews": reviews,
            "liked": liked,
            "commented": False,
            "reviews_form": Guest_reviewsForm()
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
            reviews = reviews_form.save(commit=False)
            reviews.room = room
            reviews.save()
        else:
            reviews_form = Guest_reviewsForm()

        context = {
            "room": room,
            "reviews": reviews,
            "commented": True,
            "liked": liked,
            "reviews_form": Guest_reviewsForm()
        }

        return render(request, self.template_name, context)


class BookRoomView(View):
    template_name = 'booking.html'

    def get(self, request, slug):
        room = get_object_or_404(Room, slug=slug)
        form = BookingForm()
        return render(request, self.template_name, {'room': room, 'form': form})

    def post(self, request, slug):
        room = get_object_or_404(Room, slug=slug)
        form = BookingForm(request.POST)

        if form.is_valid():
            # Создайте бронирование, установив поле customer
            booking = form.save(commit=False)
            if request.user.is_authenticated:
                booking.customer = request.user  # Используйте текущего пользователя как клиента
            booking.room = room
            booking.save()
            return redirect('success_booking')
        else:
            return render(request, self.template_name, {'room': room, 'form': form})


class SuccessBookingView(View):
    template_name = "success_booking.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
