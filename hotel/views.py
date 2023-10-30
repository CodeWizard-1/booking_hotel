from django.shortcuts import render
from django.views import generic
from .models import Room


class RoomList(generic.ListView):
    model = Room
    queryset = Room.objects.filter(status=1).order_by('-id')
    template_name = 'index.html'
    paginate_by = 6
