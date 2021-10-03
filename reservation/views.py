from django.shortcuts import render, redirect
from reservation.forms import ReservationForm
from reservation.models import Reservation


def reserve(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = ReservationForm()
    return render(request, 'index.html', {'form': form})


def show(request):
    reservations = Reservation.objects.all()
    return render(request, "show.html", {'reservations': reservations})


def edit(request, id):
    reservation = Reservation.objects.get(id=id)
    return render(request, 'edit.html', {'reservation': reservation})


def update(request, id):
    reservation = Reservation.objects.get(id=id)
    form = ReservationForm(request.POST, instance=reservation)
    if form.is_valid():
        form.save()
    return redirect("/show")

    return render(request, 'edit.html', {'reservation': reservation})


def delete(request, id):
    reservation = Reservation.objects.get(id=id)
    reservation.delete()
    return redirect("/show")
