from django.shortcuts import render, redirect
from django.views import View

from conference.models import *


# widok po wejściu na stronę pierwszy raz
class Index(View):
    def get(self, request):
        return render(request, 'index.html')


# dodawanie nowego wpisu do bazy danych AKA tworzenie nowej sali
class AddRoom(View):
    def get(self, request):
        return render(request, 'add_room.html')

    def post(self, request):

        # pobieranie danych z formularza
        room_name = request.POST.get('room_name')
        name = request.POST.get('room_name')
        capacity = request.POST.get('room_capacity')

        # przypisanie właściwej wartości do @projector w zależności od wyboru w formularzu
        if request.POST.get('room_projector') == 'yes':
            projector = True
        else:
            projector = False

        # sprawdzanie błędów i ich wyświetlanie
        if not name:
            return render(request, 'add_room.html', {'error_wrong_name': "Proszę wprowadzić poprawną nazwę sali."})
        if int(capacity) <= 0:
            return render(request, 'add_room.html', {'error_negative_number': "Pojemność musi być liczbą dodatnią."})
        if Room.objects.filter(name=name).exists():
            return render(request, 'add_room.html', {'exists': Room.objects.get(name=room_name)})

        # tworzenie nowego wpisu w bazie danych, powrót do strony formularza z wiadomością o udaniu
        # się stworzenia nowej sali
        Room.objects.create(name=name, capacity=int(capacity), projector=projector)
        return render(request, 'add_room.html', {'done': True})


# widok listy wszystkich sal
class List(View):
    def get(self, request):
        rooms = Room.objects.all().order_by('pk')
        return render(request, 'rooms.html', {'rooms': rooms})

    def post(self, request, id):
        rooms = Room.objects.all().order_by('pk')
        id = Room.objects.get(pk=id)
        return render(request, 'rooms.html', {'rooms': rooms, 'ex_room': id})


# widok informacji dot. sali
class Details(View):
    def get(self, request, id):
        id = Room.objects.get(pk=id)
        return render(request, 'room_details.html', {'room_id': id})


# widok do modyfikowania informacji nt. sali
class Modify(View):
    def get(self, request, id):
        id = Room.objects.get(pk=id)
        return render(request, 'room_modify.html', {'room_id': id})


# widok usuwania sali
class Delete(View):
    def get(self, request, id):
        id = Room.objects.get(pk=id)
        return render(request, 'room_delete.html', {'room_id': id, 'method': 'GET'})

    def post(self, request, id):
        if request.POST.get('yes'):
            Room.objects.get(pk=id).delete()
            return redirect('/room/')


# widok rezerwacji sali
class Reserve(View):
    pass
