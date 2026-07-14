from app.repositories.movie_repository import MovieRepository
from app.repositories.series_repository import SeriesRepository
from app.repositories.actor_repository import ActorRepository


class SearchService:

    @staticmethod
    def search(
        db,
        text,
    ):

        return {

            "movies":
                MovieRepository.search(
                    db,
                    text,
                ),

            "series":
                SeriesRepository.search(
                    db,
                    text,
                ),

            "actors":
                ActorRepository.search(
                    db,
                    text,
                )

        }