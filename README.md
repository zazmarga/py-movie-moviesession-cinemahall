# Movie, CinemaHall, and MovieSession

- Warning: Use `pytest app` for testing - not simple `pytest`
- Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before start

**Note**: In `main.py` you can extend but can't modify
lines 1-3.

In `db/models.py` you already have tables you created earlier. Now
you have to create tables:
1. `Movie`, with such fields:
    - char field `title`, the title of the movie with
the maximum length of 255 characters.
    - text field `description`
    - many to many field `actors`, which is related to 
the table `Actor`
    - many to many field `genres`, which is related to 
the table `Genre`

There should be implemented the string representation of the movie:
```python
speed = Movie.objects.create(title="Speed", description="Speed movie")
print(speed)
# Speed
```
2. `CinemaHall`, with such fields:
    - char field `name`, the name of the cinema hall with the maximum
length of 255 characters
    - integer field `rows`, the number of rows of seats in the
hall
    - integer field `seats_in_row`, the number of seats in each row

There should be implemented string representation of the hall and
method `capacity` that returns total number of seats in the hall:
```python
blue = CinemaHall.objects.create(name="Blue", rows=9, seats_in_row= 13) 

print(blue)
# Blue

print(blue.capacity())
# 117
```
3. `MovieSession`, with such field:
    - date time field `show_time`, the date and the time of the movie session
performance
    - foreign key `cinema_hall`, the hall where the movie session is performed,
references to the table `CinemaHall`
    - foreign key `movie`, the movie to be shown, references 
to the table `Movie`
    
There should be implemented string representation of the movie session,
that shows the movie name, the date, and the time of the movie session:

```python
import datetime

movie_session = MovieSession.objects.create(
    show_time=datetime.datetime(year=2021, month=11, day=29, hour=16, minute=40),
    cinema_hall=blue,
    movie=speed
)

print(movie_session)
# Speed 2021-11-29 16:40:00
```

Also, implement a few services for these tables. A service
represents class with static methods for the certain table.
Create such services:
1. `MovieService`, implements such methods:
   - `get_movies`, returns all movies
   - `get_movie_by_id`, takes `movie_id` - id of the movie,
returns movie with the given id.
   - `get_movies_by_genres_and_actors`, takes `genres_ids` - list
of genres ids, `actors_ids` - list of actors ids. 
       - If given both 
`genres_ids` and `actors_ids`, the method returns the queryset
with movies, that have at least one genre from `genres_ids` **and**
one actor from `actors_ids`. 
       - If only `genres_ids` is given, the method returns the queryset
with movies, that have at least one genre from `genres_ids`
       - If only `actors_ids` is given, the method returns the queryset
with movies, that have at least one actor from `actors_ids`
   - `create_movie`, takes `movie_title` and `movie_description`, creates
movie with given parameters

**Note**: You can use suffix `__id` to get access to the field `id`
of related table inside `.filter()` method. You also can 
use the suffix `__in`  to check if the value is in some list/tuple.

2. `CinemaHallService`, implements such methods:
   - `get_cinema_halls`, returns all cinema halls
   - `create_cinema_hall`, takes `hall_name`, `hall_rows`, `hall_seats_in_row`,
creates cinema hall with given parameters
3. `MovieSessionService`, implements such methods:
   - `get_movies_sessions`, returns all movies sessions
   - `get_movie_session_by_id`, takes `movie_session_id` - id of the movie, 
returns movie session with the given id
   - `get_movies_sessions_by_date`, takes string `date` in such form:
"year-month-day", returns all movie sessions performed that day.
   - `delete_movie_session_by_id`, takes `session_id` - id of session,
deletes movie session with the given id
