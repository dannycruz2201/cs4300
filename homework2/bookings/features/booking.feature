Feature: Movie Booking

  Scenario: User views movie list

    Given a movie exists

    When I visit the movie page

    Then I should see the movie


  Scenario: User can view booking history

    Given a booking exists

    When I visit booking history

    Then I should see the booking