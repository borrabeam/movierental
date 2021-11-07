import csv
from movie import Movie

class MovieCatalog:
    def __init__(self):
        self.row = open("movies.csv", "r")
        self.movies = [i for i in csv.reader(self.row)]
    
    def get_movie(self, title: str) -> Movie:
        for i in self.movies:
            if title == i[1]:
                return Movie(title, int(i[2]), i[3].split('|'))