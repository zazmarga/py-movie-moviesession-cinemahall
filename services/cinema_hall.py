from django.db.models import QuerySet

from db.models import CinemaHall


def get_cinema_halls() -> QuerySet:
    return CinemaHall.objects.all()


def create_cinema_hall(hall_name: str,
                       hall_row: int,
                       hall_seats_in_row: int
                       ) -> CinemaHall:
    return CinemaHall.objects.create(
        name=hall_name,
        row=hall_row,
        seats_in_row=hall_seats_in_row
    )
