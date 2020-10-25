from datetime import datetime

from movie.domainmodel.movie import Movie


class Review:

    def __init__(self, movie: Movie, review_text: str, rating: int):
        if type(movie) is Movie:
            self._movie = movie
        else:
            self._movie = None

        if type(review_text) is str:
            self._review_text = review_text.strip()
        else:
            self._review_text = None

        if 0 < rating <= 10:
            self._rating = rating
        else:
            self._rating = None

        self._timestamp = datetime.today()

    def __repr__(self):
        return f"<Movie {self.movie.title}, {self.movie.year}> Review: {self.review_text} Rating:{self.rating}/10 {self._timestamp}"

    def __eq__(self, other):
        return (self.movie, self.review_text, self.rating, self.timestamp) \
               == (other.movie, other.review_text, other.rating, other.timestamp)

    @property
    def movie(self):
        return self._movie

    @property
    def review_text(self):
        return self._review_text

    @property
    def rating(self):
        return self._rating

    @property
    def timestamp(self):
        return self._timestamp


