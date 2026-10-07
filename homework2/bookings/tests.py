from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from .models import (
    Movie,
    Seat,
    Booking
)


class MovieModelTest(TestCase):

    def test_movie_creation(self):

        movie = Movie.objects.create(
            title="Dune",
            description="Sci Fi",
            release_date="2024-01-01",
            duration=120
        )

        self.assertEqual(
            movie.title,
            "Dune"
        )


class SeatModelTest(TestCase):

    def test_seat_creation(self):

        seat = Seat.objects.create(
            seat_number="A1",
            booking_status=False
        )

        self.assertEqual(
            seat.seat_number,
            "A1"
        )


class BookingModelTest(TestCase):

    def test_booking_creation(self):

        user = User.objects.create_user(
            username="student"
        )

        movie = Movie.objects.create(
            title="Dune",
            description="Sci Fi",
            release_date="2024-01-01",
            duration=120
        )

        seat = Seat.objects.create(
            seat_number="B1"
        )

        booking = Booking.objects.create(
            movie=movie,
            seat=seat,
            user=user
        )

        self.assertEqual(
            booking.movie.title,
            "Dune"
        )


#view tests

class TemplateViewTests(TestCase):

    def setUp(self):

        self.movie = Movie.objects.create(
            title="Avatar",
            description="Movie",
            release_date="2024-01-01",
            duration=100
        )

    def test_movie_list_page(self):

        response = self.client.get(
            reverse('movie_list')
        )

        self.assertEqual(
            response.status_code,
            200
        )

    def test_booking_history_page(self):

        response = self.client.get(
            reverse('booking_history')
        )

        self.assertEqual(
            response.status_code,
            200
        )


#Integration Tests for API
class MovieApiTests(APITestCase):

    def test_get_movies(self):

        Movie.objects.create(
            title="Batman",
            description="Hero",
            release_date="2024-01-01",
            duration=120
        )

        response = self.client.get(
            '/api/movies/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )


    def test_create_movie(self):

        data = {
            "title": "Superman",
            "description": "DC Hero",
            "release_date": "2024-01-01",
            "duration": 130
        }

        response = self.client.post(
            '/api/movies/',
            data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )


#Booking API test
class BookingApiTests(APITestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username='student1'
        )

        self.movie = Movie.objects.create(
            title='Movie',
            description='Test',
            release_date='2024-01-01',
            duration=120
        )

        self.seat = Seat.objects.create(
            seat_number='B3'
        )


    def test_create_booking(self):

        data = {
            "movie": self.movie.id,
            "seat": self.seat.id,
            "user": self.user.id
        }

        response = self.client.post(
            '/api/bookings/',
            data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )