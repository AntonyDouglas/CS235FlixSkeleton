import pytest
from movie.domainmodel.movie import Movie
from movie.domainmodel.actor import Actor
from movie.domainmodel.genre import Genre
from movie.domainmodel.director import Director
from movie.domainmodel.review import Review
from movie.domainmodel.watchlist import WatchList

@pytest.fixture()
def test_init():
    actor1 = Actor("Horror")
    assert repr(actor1) == "<Actor Horror>"
    actor2 = Actor("")
    assert actor2.actor is None
    actor3 = Actor(42)
    assert actor3.actor is None
    actor4 = Actor("Horror")
    assert actor1 == actor4

@pytest.fixture()
def test_name():
    actor1 = Actor("Action")
    actor2 = Actor("Adventure")
    actor3 = Actor("Horror")
    print(actor1 > actor2)
    print(actor1 > actor3)
    print(actor2 < actor3)


@pytest.fixture()
def test_add_colleague():
    actor1 = Actor("Action")
    actor2 = Actor("Adventure")
    actor1.add_actor_colleague(actor2)
    assert actor1.check_if_this_actor_worked_with(actor2) == True

pytest.fixture()
def test_add_movie():
    movie1 = Movie("Moana", 2016)
    movie2 = Movie("Ice Age", 2002)
    movie3 = Movie("Wall-E", 2008)

    watchlist = WatchList()
    watchlist.add_movie(movie1)
    watchlist.add_movie(movie2)
    watchlist.add_movie(movie3)
    watchlist.add_movie("abc")
    watchlist.add_movie(123)

    assert watchlist.size() == 3
    assert watchlist.watchlist == [movie1, movie2, movie3]

@pytest.fixture()
def test_director():
    director1 = Director("Taika Waititi")
    assert repr(director1) == "<Director Taika Waititi>"
    director2 = Director("")
    assert director2.director_full_name is None
    director3 = Director(42)
    assert director3.director_full_name is None



