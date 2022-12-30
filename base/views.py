from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm

# Create your views here.

def home(request):
    rooms = Room.objects.all()
    context = {"rooms": rooms}
    return render(request, "base/home.html", context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {"room": room}
    return render(request, "base/room.html", context)

def createRoom(request):
    form = RoomForm()
    if request.method == "POST":
        
        # Extracts all POST values from the form
        form = RoomForm(request.POST)
        if form.is_valid():

            # Saves the data to the database
            form.save()
            return redirect("home")


    context = {"form": form}
    return render(request, "base/room_form.html", context)

def updateRoom(request, pk):
    room = Room.objects.get(id=pk)

    # Prefills data with existing room fields
    form = RoomForm(instance=room)

    if request.method == "POST":

        # When recieving form data you can pass an instance to determine what ID to update
        # Note: By using an instance you convert the creation to an override
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"form": form}
    return render(request, "base/room_form.html", context)

def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == "POST":

        # Objects have a delete property that can delete elements from the database
        room.delete()
        return redirect("home")

    return render(request, "base/delete.html", {"obj": room})