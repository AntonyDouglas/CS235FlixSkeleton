from movie.domainmodel.movie import Movie
from movie.domainmodel.review import Review


class User:

    def __init__(self, user_name: str, password: str):
        if type(user_name) is str and len(user_name) > 0:
            self._user_name = user_name.lower().strip()
        else:
            self._user_name = None

        if type(password) is str and len(password) > 0:
            self._password = password
        else:
            self._password = None

        self._watched_movies = []
        self._reviews = []
        self._time_spent_watching_movies_minutes = 0

    @property
    def user_name(self):
        return self._user_name

    @property
    def password(self):
        return self._password

    @property
    def reviews(self):
        return self._reviews

    @property
    def time_spent_watching_movies_minutes(self):
        return self._time_spent_watching_movies_minutes

    @property
    def watched_movies(self):
        return self._watched_movies

    def __repr__(self):
        return f"<User {self._user_name}>"

    def __eq__(self, other):
        return self._user_name == other.user_name

    def __lt__(self, other):
        return self._user_name < other.user_name

    def __hash__(self):
        return hash(self._user_name)

    def watch_movie(self, movie):
        if type(movie) is Movie:
            if movie not in self.watched_movies:
                self.watched_movies.append(movie)
            self._time_spent_watching_movies_minutes += movie.runtime_minutes
            movie.times_watched = 1

    def add_review(self, review):
        if type(review) is Review:
            self._reviews.append(review)


