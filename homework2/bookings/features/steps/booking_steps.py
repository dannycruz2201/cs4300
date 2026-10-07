from behave import *

from bookings.models import (
    Movie,
    Seat,
    Booking
)

from django.contrib.auth.models import User


@given('a movie exists')
def step_impl(context):

    Movie.objects.create(
        title="Dune",
        description="Movie",
        release_date="2024-01-01",
        duration=120
    )


@when('I visit the movie page')
def step_impl(context):

    context.response = context.test.client.get('/api/')


@then('I should see the movie')
def step_impl(context):
    assert b'Dune' in context.response.content


@given('a booking exists')
def step_impl(context):
    # Create Movie
    movie = Movie.objects.create(
        title="Test Movie",
        description="A test movie",
        release_date="2024-01-01",
        duration=120
    )
    
    # Create a seat
    seat = Seat.objects.create(
        seat_number="A1",
        booking_status=False
    )
    
    # Create a user
    user = User.objects.create_user(
        username='testuser',
        password='testpass'
    )
    
    # booking linking the movie, seat, and user
    Booking.objects.create(
        movie=movie,
        seat=seat,
        user=user
    )

@when('I visit booking history')
def step_impl(context):
    # GET request to the bookings history endpoint
    context.response = context.test.client.get('/api/history/')

@then('I should see the booking')
def step_impl(context):
   
    #Check booking test movie in response
    assert b'Test Movie' in context.response.content
