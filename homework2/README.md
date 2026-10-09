# Movie Theater Booking Application

## Overview

This project is a RESTful Movie Theater Booking Application built using Django and Django REST Framework.

The application allows users to:

- View movie listings
- Check seat availability
- Book seats
- View booking history

The application includes:

- REST API endpoints
- Django template-based web interface using Bootstrap

## Features

### User Interface

- Movie Listing Page
- Seat Booking Page
- Booking History Page
- Bootstrap Responsive Design

### REST API

- List Movies
- Create Movies
- Update Movies
- Delete Movies
- View Seats
- Book Seats
- Create Bookings
- View Booking History

## Technologies Used

- Python
- Django
- Django REST Framework
- Bootstrap 5
- SQLite
- Behave
- Render

## Project Structure

```text
homework2/
│
├── bookings/
│   ├── migrations/
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── forms.py
│   ├── urls.py
│   └── tests.py
│
├── features/
│   └── BDD Tests
│
├── movie_theater_booking/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── build.sh
├── manage.py
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/dannycruz2201/cs4300.git
```

Move into the project:

```bash
cd homework2
```

Activate the existing virtual environment:

```bash
source venv/bin/activate
```

If a virtual environment does not exist:

```bash
python3 -m venv venv --system-site-packages
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Database Setup

Create migrations:

```bash
python manage.py makemigrations
```

Apply migrations:

```bash
python manage.py migrate
```

Create administrator account:

```bash
python manage.py createsuperuser
```

## Running Locally

Start Django:

```bash
python3 manage.py runserver 0.0.0.0:3000
```

If using DevEdu, open the application using the DevEdu App URL generated from the App button.

If running locally outside DevEdu, open:

```text
http://127.0.0.1:3000/
```

## Web Pages

### Home

```text
/
```

### Seat Booking

```text
/movie/<movie_id>/
```

### Booking History

```text
/history/
```

## API Endpoints

### Movies

```text
/api/movies/
```

### Seats

```text
/api/seats/
```

### Bookings

```text
/api/bookings/
```

## Unit Testing

Run:

```bash
python manage.py test
```

## Behavior Driven Testing

Run:

```bash
python manage.py behave
```

## Deployment

The application is deployed using Render.

### Render URL

https://movie-theater-booking-uh22.onrender.com/

## GitHub Repository

https://github.com/dannycruz2201/cs4300

## AI Usage Disclosure

Microsoft Copilot was used during development for:

- Django project guidance
- Django REST Framework guidance
- Unit test templates
- Behave testing templates
- Render deployment guidance
- README editing and verification

All generated content was reviewed, tested, modified, and validated before inclusion in the final submission.

## Assignment Requirements Checklist

- [x] Models Implemented
- [x] Serializers Implemented
- [x] ViewSets Implemented
- [x] REST API Created
- [x] Django Templates Created
- [x] Bootstrap UI Added
- [x] Unit Tests Implemented
- [x] Integration Tests Implemented
- [x] BDD Tests Implemented
- [x] Render Deployment Completed
- [x] README Completed
