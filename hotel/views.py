from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Room, Guest_reviews, City
from .forms import Guest_reviewsForm


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