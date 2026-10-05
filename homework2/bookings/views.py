from rest_framework import viewsets
from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Seat, Booking
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

    seats = Seat.objects.all()

    return render(
        request,
        'bookings/seat_booking.html',
        {
            'movie': movie,
            'seats': seats
        }
    )

def booking_history(request):

    bookings = Booking.objects.all()

    return render(
        request,
        'bookings/booking_history.html',
        {'bookings': bookings}
    )