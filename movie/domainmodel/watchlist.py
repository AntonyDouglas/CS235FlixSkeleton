from movie.domainmodel.movie import Movie


class WatchList:
    def __init__(self):
        self._watchlist = []
        self.index = 0

    def __repr__(self):
        return f"Watchlist: {self._watchlist}"

    @property
    def watchlist(self):
        return self._watchlist

    def add_movie(self, movie):
        if type(movie) is Movie and movie not in self._watchlist:
            self._watchlist.append(movie)

    def remove_movie(self, movie):
        if movie in self._watchlist:
            self._watchlist.remove(movie)

    def select_movie_to_watch(self, index):
        if type(index) is not int:
            return None
        elif index >= len(self._watchlist) or index <= -1:
            return None
        else:
            return self._watchlist[index]

    def size(self):
        return len(self._watchlist)

    def first_movie_in_watchlist(self):
        if len(self._watchlist) <= 0:
            return None
        else:
            return self._watchlist[0]

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self._watchlist):
            raise StopIteration
        else:
            movie_at_index = self._watchlist[self.index]
            self.index += 1
            return movie_at_index
