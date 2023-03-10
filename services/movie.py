from typing import List

from django.db.models import QuerySet

from db.models import Genre, Actor, Movie


def get_movies(
    genres_ids: List[Genre] = None, actors_ids: List[Actor] = None
) -> QuerySet:
    movies = Movie.objects.all()

    if genres_ids and actors_ids:
        movies = movies.filter(
            genres__id__in=genres_ids, actors__id__in=actors_ids
        ).distinct()
    elif genres_ids:
        movies = movies.filter(genres__id__in=genres_ids).distinct()
    elif actors_ids:
        movies = movies.filter(actors__id__in=actors_ids).distinct()

    return movies


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
    movie_title: str,
    movie_description: str,
    genres_ids: list[int] = None,
    actors_ids: list[int] = None,
) -> None:
    movie = Movie.objects.create(
        title=movie_title, description=movie_description
    )
    if genres_ids:
        movie.genres.set(Genre.objects.filter(id__in=genres_ids))
    if actors_ids:
        movie.actors.set(Actor.objects.filter(id__in=actors_ids))