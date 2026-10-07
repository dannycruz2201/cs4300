from rest_framework import viewsets
from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Seat, Booking
from django.contrib.auth.models import User
from .forms import SeatBookingForm
from .serializers import (
    MovieSerializer,
    SeatSerializer,
    BookingSerializer
)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


def movie_list(request):
    movies = Movie.objects.all()

    return render(
        request,
        'bookings/movie_list.html',
        {'movies': movies}
    )


def seat_booking(request, movie_id):

    movie = get_object_or_404(
        Movie,
        id=movie_id
    )

    if request.method == "POST":

        form = SeatBookingForm(request.POST)

        if form.is_valid():

            seat = form.cleaned_data["seat"]

            if not seat.booking_status:

                seat.booking_status = True
                seat.save()

                user = User.objects.first()#later add log in functionality

                Booking.objects.create(
                    movie=movie,
                    seat=seat,
                    user=user
                )

                return redirect(
                    'booking_history'
                )

    else:

        form = SeatBookingForm()

    seats = Seat.objects.all()

    return render(
        request,
        'bookings/seat_booking.html',
        {
            'movie': movie,
            'seats': seats,
            'form': form
        }
    )

def booking_history(request):

    bookings = Booking.objects.select_related(
        'movie',
        'seat',
        'user'
    )

    return render(
        request,
        'bookings/booking_history.html',
        {
            'bookings': bookings
        }
    )