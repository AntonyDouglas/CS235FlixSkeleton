from movie.domainmodel.user import User
from movie.domainmodel.movie import Movie


class movie_compare:

    def __init__(self, movies_lst: list):
        if type(movies_lst) is not list:
            self._movies_lst = []
        else:
            self._movies_lst = [x for x in movies_lst if type(x) is Movie]

    def __repr__(self):
        string = ""
        for movie in self._movies_lst:
            string += f" {str(movie)}\n"

        return string

    @property
    def movies_lst(self):
        return self._movies_lst

    def most_watched(self):
        temp = None
        rank = 1
        for i in range(0, len(self._movies_lst)):
            for j in range(i + 1, len(self._movies_lst)):
                if self._movies_lst[i].times_watched < self._movies_lst[j].times_watched:
                    temp = self._movies_lst[i]
                    self._movies_lst[i] = self._movies_lst[j]
                    self._movies_lst[j] = temp

                elif self._movies_lst[i].times_watched == self._movies_lst[j].times_watched:
                    if self._movies_lst[i].title > self._movies_lst[j].title:
                        temp = self._movies_lst[i]
                        self._movies_lst[i] = self._movies_lst[j]
                        self._movies_lst[j] = temp

        for movie in self._movies_lst:
            print(f"{rank}. {str(movie)} {str(movie.times_watched)} views")
            rank += 1

    def least_watched(self):
        temp = None
        rank = 1
        for i in range(0, len(self._movies_lst)):
            for j in range(i + 1, len(self._movies_lst)):
                if (self._movies_lst[i].times_watched, self._movies_lst[i].title) > (
                        self._movies_lst[j].times_watched, self._movies_lst[j].title):
                    temp = self._movies_lst[i]
                    self._movies_lst[i] = self._movies_lst[j]
                    self._movies_lst[j] = temp

        for movie in self._movies_lst:
            print(f"{rank}. {str(movie)} {movie.times_watched} views")
            rank += 1

    def longest_movie(self):
        temp = None
        rank = 1
        for i in range(0, len(self._movies_lst)):
            for j in range(i + 1, len(self._movies_lst)):
                if self._movies_lst[i].runtime_minutes < self._movies_lst[j].runtime_minutes:
                    temp = self._movies_lst[i]
                    self._movies_lst[i] = self._movies_lst[j]
                    self._movies_lst[j] = temp

                elif self._movies_lst[i].runtime_minutes == self._movies_lst[j].runtime_minutes:
                    if self._movies_lst[i].title > self._movies_lst[j].title:
                        temp = self._movies_lst[i]
                        self._movies_lst[i] = self._movies_lst[j]
                        self._movies_lst[j] = temp

        for movie in self._movies_lst:
            print(f"{rank}. {str(movie)} {movie.runtime_minutes} minutes")
            rank += 1

    def shortest_movie(self):
        temp = None
        rank = 1
        for i in range(0, len(self._movies_lst)):
            for j in range(i + 1, len(self._movies_lst)):
                if (self._movies_lst[i].runtime_minutes, self._movies_lst[i].title) > (
                        self._movies_lst[j].runtime_minutes, self._movies_lst[j].title):
                    temp = self._movies_lst[i]
                    self._movies_lst[i] = self._movies_lst[j]
                    self._movies_lst[j] = temp

        for movie in self._movies_lst:
            print(f"{rank}. {str(movie)} {movie.runtime_minutes} minutes")
            rank += 1



user1 = User("John", "abc123")
user2 = User("Mike", "abcd123")
user3 = User("Sam", "bebebebe")

movie1 = Movie("Moana", 2016)
movie2 = Movie("Ice Age", 2002)
movie3 = Movie("John Cena", 1999)
movie4 = Movie("Bravo", 2000)
movie5 = Movie("Charlie", 1987)
movie6 = Movie("Alpha", 2010)

movie1.runtime_minutes = 120
movie2.runtime_minutes = 120
movie3.runtime_minutes = 114
movie4.runtime_minutes = 180
movie5.runtime_minutes = 86
movie6.runtime_minutes = 12


user1.watch_movie(movie1)
user1.watch_movie(movie2)
user1.watch_movie(movie2)
user1.watch_movie(movie2)
user1.watch_movie(movie2)
user1.watch_movie(movie2)

user2.watch_movie(movie2)
user2.watch_movie(movie3)

user3.watch_movie(movie3)

movie_lst = [movie1, movie2, movie3, movie4, movie5, movie6]
movie_comparison = movie_compare(movie_lst)
movie_comparison.longest_movie()
