from movie.domainmodel.genre import Genre
from movie.domainmodel.actor import Actor
from movie.domainmodel.director import Director


class Movie:

    def __init__(self, title: str, year: int):
        if type(title) is str and len(title) > 0:
            self._title = title.strip()
        else:
            self._title = None

        if type(year) is int and year >= 1900:
            self._year = year
        else:
            self._year = None

        self._director = None
        self._actors = []
        self._genres = []
        self._description = None
        self._runtime_minutes = 0

        self._times_watched = 0

    def __repr__(self):
        return f"<Movie {self._title}, {self._year}>"

    def __eq__(self, other):
        if self._title == other.title and self._year == other.year:
            return True
        else:
            return False

    def __lt__(self, other):
        return (self._title, self._year) < (other.title, other.year)

    def __hash__(self):
        return hash(self._title + str(self._year))


    @property
    def title(self):
        return self._title

    @property
    def times_watched(self):
        return self._times_watched

    @property
    def year(self):
        return self._year

    @property
    def runtime_minutes(self):
        return self._runtime_minutes

    @property
    def actors(self):
        return self._actors

    @property
    def genres(self):
        return self._genres

    @property
    def director(self):
        return self._director

    @property
    def description(self):
        return self._description

    @times_watched.setter
    def times_watched(self, count):
        if count == 1:
            self._times_watched += count

    @runtime_minutes.setter
    def runtime_minutes(self, minutes):
        if type(minutes) is int and minutes > 0:
            self._runtime_minutes = minutes
        else:
            raise ValueError()

    @title.setter
    def title(self, string):
        if type(string) is str and len(string) > 0:
            self._title = string.strip()

    @description.setter
    def description(self, new_description):
        if type(new_description) is str and len(new_description) > 0:
            self._description = new_description.strip()

    @director.setter
    def director(self, new_director):
        if type(new_director) is Director:
            self._director = new_director

    def add_actor(self, new_actor):
        if type(new_actor) is Actor:
            self.actors.append(new_actor)

    def remove_actor(self, rem_actor):
        if rem_actor in self.actors:
            self.actors.remove(rem_actor)

    def add_genre(self, new_genre):
        if type(new_genre) is Genre:
            self.genres.append(new_genre)

    def remove_genre(self, rem_genre):
        if rem_genre in self.genres:
            self.genres.remove(rem_genre)



