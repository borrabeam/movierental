import csv
from movie import Movie

class MovieCatalog:
    def __init__(self):
        self.row = open("movies.csv", "r")
        self.movies = [i for i in csv.reader(self.row)]
    
    def get_movie(self, title: str):
        for i in self.movies:
            if title == i[1]:
                return i