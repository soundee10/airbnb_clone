from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone
from django.views.generic import ListView
from django.http import HttpResponse, Http404
from . import models

# Create your views here.


class HomeView(ListView):
    """Homeview Description"""

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    #   page_kwarg = "potato"
    context_object_name = "rooms"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        context["now"] = now

        return context


def room_detail(request, pk):
    try:
        room = models.Room.objects.get(pk=pk)
        return render(request, "rooms/detail.html", {"room": room})
    except models.Room.DoesNotExist:
        raise Http404()
        # return redirect(reverse("core:home"))
