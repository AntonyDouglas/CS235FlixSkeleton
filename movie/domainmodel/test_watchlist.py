from movie.domainmodel.movie import Movie
from movie.domainmodel.watchlist import WatchList


class Test_watchlist_methods:

    def test_add_movie(self):
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


    def test_remove_movie(self):
        movie1 = Movie("Moana", 2016)
        movie2 = Movie("Ice Age", 2002)
        movie3 = Movie("Wall-E", 2008)

        watchlist = WatchList()
        watchlist.add_movie(movie1)
        watchlist.add_movie(movie2)
        watchlist.add_movie(movie3)

        watchlist.remove_movie(movie1)
        assert watchlist.watchlist == [movie2, movie3]
        assert watchlist.size() == 2

    def test_select_movie_to_watch(self):
        movie1 = Movie("Moana", 2016)
        movie2 = Movie("Ice Age", 2002)
        movie3 = Movie("Wall-E", 2008)

        watchlist = WatchList()
        watchlist.add_movie(movie1)
        watchlist.add_movie(movie2)
        watchlist.add_movie(movie3)

        assert watchlist.select_movie_to_watch(0) == movie1
        assert watchlist.select_movie_to_watch(90) is None
        assert watchlist.select_movie_to_watch("abc") is None
        assert watchlist.select_movie_to_watch(-1) is None

    def test_size(self):
        movie1 = Movie("Moana", 2016)
        movie2 = Movie("Ice Age", 2002)
        movie3 = Movie("Wall-E", 2008)

        watchlist = WatchList()
        watchlist.add_movie(movie1)
        watchlist.add_movie(movie2)
        watchlist.add_movie(movie3)

        assert watchlist.size() == 3


    def test_first_movie_in_watchlist(self):
        movie1 = Movie("Moana", 2016)
        movie2 = Movie("Ice Age", 2002)
        movie3 = Movie("Wall-E", 2008)

        watchlist = WatchList()
        watchlist.add_movie(movie1)
        watchlist.add_movie(movie2)
        watchlist.add_movie(movie3)

        assert watchlist.first_movie_in_watchlist() == movie1


    def test_iter_next(self):
        movie1 = Movie("Moana", 2016)
        movie2 = Movie("Ice Age", 2002)
        movie3 = Movie("Wall-E", 2008)

        watchlist = WatchList()
        watchlist.add_movie(movie1)
        watchlist.add_movie(movie2)
        watchlist.add_movie(movie3)

        new_lst = []

        for i in watchlist.watchlist:
            print(i)
            new_lst.append(i)

        assert new_lst == [movie1, movie2, movie3]