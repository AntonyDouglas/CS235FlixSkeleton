from movie.domainmodel.movie import Movie
from movie.domainmodel.user import User
from movie.domainmodel.movie_compare import movie_compare
import pytest


class Test_movie_compare_methods:

    def test_init(self):
        movie1 = Movie("Moana", 2016)
        movie2 = Movie("Ice Age", 2002)
        movie3 = Movie("John Cena", 1999)
        movie4 = Movie("Bravo", 2000)
        movie5 = Movie("Charlie", 1987)

        not_movie = "Hello World"
        not_movie2 = 123

        lst = [movie1, movie2, movie3, movie4, movie5, not_movie, not_movie2]

        not_lst = "string"
        film_compare1 = movie_compare(not_lst)

        assert film_compare1.movies_lst == []

        film_comparison2 = movie_compare(lst)
        assert film_comparison2.movies_lst == [movie1, movie2, movie3, movie4, movie5]

    def test_most_watched(self):

        user1 = User("John", "abc123")
        user2 = User("Mike", "abcd123")
        user3 = User("Sam", "bebebebe")

        movie1 = Movie("Moana", 2016)
        movie2 = Movie("Ice Age", 2002)
        movie3 = Movie("John Cena", 1999)
        movie4 = Movie("Bravo", 2000)
        movie5 = Movie("Charlie", 1987)

        user1.watch_movie(movie1)

        user1.watch_movie(movie2)
        user1.watch_movie(movie2)
        user1.watch_movie(movie2)
        user1.watch_movie(movie2)
        user1.watch_movie(movie2)
        user2.watch_movie(movie2)

        user2.watch_movie(movie3)
        user3.watch_movie(movie3)

        lst = [movie1, movie2, movie3, movie4, movie5]

        film_comparison = movie_compare(lst)
        film_comparison.most_watched()

        assert film_comparison.movies_lst == [movie2, movie3, movie1, movie4, movie5]

    def test_least_watched(self):
        user1 = User("John", "abc123")
        user2 = User("Mike", "abcd123")
        user3 = User("Sam", "bebebebe")

        movie1 = Movie("Moana", 2016)
        movie2 = Movie("Ice Age", 2002)
        movie3 = Movie("John Cena", 1999)
        movie4 = Movie("Bravo", 2000)
        movie5 = Movie("Charlie", 1987)

        user1.watch_movie(movie1)

        user1.watch_movie(movie2)
        user1.watch_movie(movie2)
        user1.watch_movie(movie2)
        user1.watch_movie(movie2)
        user1.watch_movie(movie2)
        user2.watch_movie(movie2)

        user2.watch_movie(movie3)
        user3.watch_movie(movie3)

        lst = [movie1, movie2, movie3, movie4, movie5]

        film_comparison = movie_compare(lst)
        film_comparison.least_watched()

        assert film_comparison.movies_lst == [movie4, movie5, movie1, movie3, movie2]



    def test_longest_movie(self):
        movie1 = Movie("Moana", 2016)
        movie2 = Movie("Ice Age", 2002)
        movie3 = Movie("John Cena", 1999)
        movie4 = Movie("Bravo", 2000)
        movie5 = Movie("Charlie", 1987)

        movie1.runtime_minutes = 120
        movie2.runtime_minutes = 120
        movie3.runtime_minutes = 114
        movie4.runtime_minutes = 180
        movie5.runtime_minutes = 86

        lst = [movie1, movie2, movie3, movie4, movie5]
        film_comparison = movie_compare(lst)
        film_comparison.longest_movie()

        assert film_comparison.movies_lst == [movie4, movie2, movie1, movie3, movie5]


    def test_shortest_movie(self):
        movie1 = Movie("Moana", 2016)
        movie2 = Movie("Ice Age", 2002)
        movie3 = Movie("John Cena", 1999)
        movie4 = Movie("Bravo", 2000)
        movie5 = Movie("Charlie", 1987)

        movie1.runtime_minutes = 120
        movie2.runtime_minutes = 120
        movie3.runtime_minutes = 114
        movie4.runtime_minutes = 180
        movie5.runtime_minutes = 86

        lst = [movie1, movie2, movie3, movie4, movie5]
        film_comparison = movie_compare(lst)
        film_comparison.shortest_movie()

        assert film_comparison.movies_lst == [movie5, movie3, movie2, movie1, movie4]

