from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from app.database import Base


class Director(Base):

    __tablename__ = "directors"

    id = Column(Integer, primary_key=True)

    name = Column(String)

    country = Column(String)

    movies = relationship(
        "Movie",
        back_populates="director",
    )

    series = relationship(
        "Series",
        back_populates="director",
    )


class Movie(Base):

    __tablename__ = "movies"

    id = Column(Integer, primary_key=True)

    title = Column(String)

    release_year = Column(Integer)

    rating = Column(Integer)

    director_id = Column(
        Integer,
        ForeignKey("directors.id"),
    )

    director = relationship(
        "Director",
        back_populates="movies",
    )


class Series(Base):

    __tablename__ = "series"

    id = Column(Integer, primary_key=True)

    title = Column(String)

    release_year = Column(Integer)

    seasons = Column(Integer)

    director_id = Column(
        Integer,
        ForeignKey("directors.id"),
    )

    director = relationship(
        "Director",
        back_populates="series",
    )

class Actor(Base):

    __tablename__ = "actors"

    id = Column(Integer, primary_key=True)

    name = Column(String)

    age = Column(Integer)