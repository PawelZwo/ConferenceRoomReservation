from django.shortcuts import render, redirect
from django.views import View

from conference.models import *


class Index(View):
    def get(self, request):
        return render(request, 'index.html')


class AddRoom(View):
    def get(self, request):
        return render(request, 'add_room.html')

    def post(self, request):
        room_name = request.POST.get('room_name')
        name = request.POST.get('room_name')
        capacity = request.POST.get('room_capacity')

        if request.POST.get('room_projector') == 'yes':
            projector = True
        else:
            projector = False
        print("pobrano dane")

        if Room.objects.filter(name=name).exists():
            return render(request, 'add_room.html', {'exists': Room.objects.get(name=room_name)})

        Room.objects.create(name=name, capacity=int(capacity), projector=projector)
        print("dodano wpis")
        return render(request, 'add_room.html', {'done': True})


class List(View):
    def get(self, request):
        rooms = Room.objects.all().order_by('pk')
        return render(request, 'rooms.html', {'rooms': rooms})


class Modify(View):
    def get(self, request):
        rooms = Room.objects.all().order_by('pk')
        return render(request, 'room_modify.html', {'rooms': rooms})


class Details(View):
    def get(self, request):
        room_details = request.GET.get(pk=room.id)
        return render(request, 'room_details.html', {'id': room_details})
