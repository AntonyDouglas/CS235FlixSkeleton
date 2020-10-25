import pytest
from movie.domainmodel.actor import Actor
from movie.domainmodel.genre import Genre
from movie.domainmodel.director import Director
from movie.domainmodel.movie import Movie
from movie.domainmodel.review import Review
from movie.domainmodel.user import User

@pytest.fixture()
def user():
    return User("john", "pass1234")

@pytest.fixture()
def test_add_actor():

    actor1 = Actor("John Cena")
    actor2 = Actor("Bill Billson")
    actor1.add_actor_colleague(actor2)
    assert (len(actor1.colleagues == 1))
    assert (len(actor2.colleagues == 1))
    assert actor1.check_if_this_actor_worked_with(actor2) == True




