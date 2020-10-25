class Genre:

    def __init__(self, genre: str):
        if genre == "" or type(genre) is not str:
            self.__genre = None
        else:
            self.__genre = genre.strip()

    def genre(self) -> str:
        return self.__genre

    def __repr__(self):
        return f"<Genre {self.__genre}>"

    def __eq__(self, other):
        return self.__genre == other.__genre

    def __lt__(self, other):
        if self.__genre is not None and other.__genre is not None:
            return self.__genre < other.__genre
        else:
            return False

    def __hash__(self):
        return hash(self.__genre)
