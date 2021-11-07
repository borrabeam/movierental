from movie import Movie
from enum import Enum
import logging
import datetime


class PriceCode(Enum):
	"""An enumeration for different kinds of movies and their behavior"""
	new_release = { "price": lambda days: 3.0*days, 
					"frp": lambda days: days}
	normal = { "price": lambda days: 2.0 if days <= 2 else 2.0 + (1.5 * (days-2)),
               "frp": lambda days: 1}
	childrens = { "price": lambda days: 1.5 if days <= 3 else 1.5 + (1.5 * (days-3)),
                  "frp": lambda days: 1}

	def price(self, days: int):
		"Return the rental price for a given number of days"""
		pricing = self.value["price"]    # the enum member's price formula
		return pricing(days)
	
	def points(self, days: int):
		"""Return the point of rental given by number of days."""
		point = self.value["frp"] # the enum member's point formula'
		return point(days)
	
	@classmethod
	def for_movie(self, movie: Movie):
		current_year = datetime.datetime.now().year
		if movie.get_year() == current_year:
			return PriceCode.new_release
		elif movie.get_genre('Children'):
			return PriceCode.childrens
		else:
			return PriceCode.normal



class Rental:
	"""
	A rental of a movie by customer.
	From Fowler's refactoring example.

	A realistic Rental would have fields for the dates
	that the movie was rented and returned, from which the
	rental period is calculated.
	But for simplicity of the example only a days_rented
	field is used.
	"""
	
	def __init__(self, movie, days_rented): 
		"""Initialize a new movie rental object for
		   a movie with known rental period (daysRented).
		"""
		self.movie = movie
		self.days_rented = days_rented
		self.price_code = PriceCode.for_movie(self.movie)
		if not isinstance(self.get_movie_title(), PriceCode):
			log = logging.getLogger()
			log.error(f"Movie {self.get_movie_title()} has unrecognized priceCode {self.price_code}")
          

	def get_movie(self):
		return self.movie
	
	def get_movie_title(self):
		return self.movie.get_title()

	def get_days_rented(self):
		return self.days_rented

	def get_price(self):
		return self.price_code.price(self.days_rented)

	def get_point(self):
		return self.price_code.points(self.days_rented)

