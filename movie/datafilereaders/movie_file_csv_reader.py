import csv

from movie.domainmodel.movie import Movie
from movie.domainmodel.actor import Actor
from movie.domainmodel.genre import Genre
from movie.domainmodel.director import Director


class MovieFileCSVReader:

    def __init__(self, file_name: str):
        self.dataset_of_directors = []
        self.dataset_of_genres = []
        self.dataset_of_actors = []
        self.dataset_of_movies = []
        self.dataset_of_descriptions = []
        self.file_name = file_name

    @property
    def dataset_of_descriptions(self):
        return self._dataset_of_descriptions

    @dataset_of_descriptions.setter
    def dataset_of_descriptions(self, desc_list):
        self._dataset_of_descriptions = desc_list

    @property
    def dataset_of_movie(self):
        return self.dataset_of_movies

    @dataset_of_movie.setter
    def dataset_of_movie(self, lst):
        if isinstance(lst, list):
            self.movies = lst

    def read_csv_file(self):
        with open(self.file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)

            index = 0
            for row in movie_file_reader:
                director = row['Director']
                genres = row['Genre']
                actors = row['Actors']
                title = row['Title']
                desc = row['Description']
                release_year = int(row['Year'])

                movie = Movie(title, release_year)
                director_obj = Director(director)

                if desc not in self.dataset_of_descriptions:
                    self.dataset_of_descriptions.append(desc)

                if movie not in self.dataset_of_movies:
                    self.dataset_of_movies.append(movie)

                if director_obj not in self.dataset_of_directors:
                    self.dataset_of_directors.append(director_obj)

                for gen in genres.split(','):
                    genre = Genre(gen)
                    if genre not in self.dataset_of_genres:
                        self.dataset_of_genres.append(genre)

                for name in actors.split(","):
                    actor = Actor(name)
                    if actor not in self.dataset_of_actors:
                        self.dataset_of_actors.append(actor)

                index += 1




