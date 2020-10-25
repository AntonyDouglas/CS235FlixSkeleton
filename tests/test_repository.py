import pytest
from movie.domainmodel.movie import Movie
from movie.domainmodel.actor import Actor
from movie.domainmodel.genre import Genre
from movie.domainmodel.director import Director
from movie.domainmodel.review import Review
from movie.domainmodel.watchlist import WatchList
from movie.repository.memoryrepository import MemoryRepository


x = MemoryRepository('tests/datafiles/Data1000Movies.csv')

@pytest.fixture()
def test_repository():
    assert len(x.movie_lst) == 1000
    assert len(x.director_lst) == 644
    assert len(x.genre_lst) == 20
    assert len(x.actor_lst) == 1985





