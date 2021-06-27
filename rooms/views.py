from math import ceil
from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse
from . import models

# Create your views here.


def all_rooms(request):
    page = request.GET.get("page")
    # page = int(page or 1)
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10, orphans=3)
    rooms = paginator.get_page(page)
    # print(vars(rooms.paginator))
    return render(request, "rooms/home.html", {"pages": rooms})
