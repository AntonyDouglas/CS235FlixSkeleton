from movie.datafilereaders.movie_file_csv_reader import MovieFileCSVReader


class MemoryRepository:
    def __init__(self, filename):

        movie_file_reader = MovieFileCSVReader(filename)
        movie_file_reader.read_csv_file()
        self.movie_lst = movie_file_reader.dataset_of_movie
        self.actor_lst = movie_file_reader.dataset_of_actors
        self.director_lst = movie_file_reader.dataset_of_directors
        self.genre_lst = movie_file_reader.dataset_of_genres
        self._desc_lst = movie_file_reader.dataset_of_descriptions

    @property
    def movie_lsts(self):
        return self.movie_lst

    @movie_lsts.setter
    def movie_lsts(self, value):
        self.movie_lst = value

    @property
    def desc_lst(self):
        return self._desc_lst

    @desc_lst.setter
    def desc_lst(self, value):
        self._desc_lst = value



