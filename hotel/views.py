from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Room, Guest_reviews


class RoomList(generic.ListView):
    model = Room
    queryset = Room.objects.filter(status=1).order_by('-id')
    template_name = 'index.html'
    paginate_by = 6


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
            "liked": liked
        }

        return render(request, self.template_name, context)
