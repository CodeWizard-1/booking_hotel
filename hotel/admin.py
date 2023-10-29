from django.contrib import admin
from .models import Room
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Room)
class RoomAdmin(SummernoteModelAdmin):
    summernote_fields = ('description_room',)


