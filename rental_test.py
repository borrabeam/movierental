import unittest
from customer import Customer
from rental import Rental, PriceCode
from movie import Movie
from movie_catalog import MovieCatalog


class RentalTest(unittest.TestCase):
	
	def setUp(self):
		self.new_movie = Movie("Mulan", 2020)
		self.regular_movie = Movie("CitizenFour", 2010)
		self.childrens_movie = Movie("Frozen", 2016)
		self.catalog = MovieCatalog()

	def test_movie_attributes(self):
		"""trivial test to catch refactoring errors or change in API of Movie"""
		m = Movie("CitizenFour", PriceCode.normal)
		self.assertEqual("CitizenFour", self.regular_movie.get_title())
		self.assertEqual(2010, self.regular_movie.get_year())
		self.assertEqual("Mulan", self.new_movie.get_title())
		self.assertEqual(2020, self.new_movie.get_year())

	
	def test_rental_price(self):
		rental = Rental(self.new_movie, 1)
		self.assertEqual(rental.get_price(), 3.0)
		rental = Rental(self.new_movie, 5)
		self.assertEqual(rental.get_price(), 15.0)

		rental_regular = Rental(self.regular_movie, 1)
		self.assertEqual(rental_regular.get_price(), 2.0)
		rental_regular = Rental(self.regular_movie, 5)
		self.assertEqual(rental_regular.get_price(), 6.5)

		rental_children = Rental(self.childrens_movie, 1)
		self.assertEqual(rental_children.get_price(), 1.5)
		rental_children = Rental(self.childrens_movie, 5)
		self.assertEqual(rental_children.get_price(), 4.5)

	
	def test_rental_points(self):
		rental = Rental(self.new_movie, 1)
		self.assertEqual(rental.get_point(), 1.0)
		rental = Rental(self.new_movie, 5)
		self.assertEqual(rental.get_point(), 5.0)

		rental_regular = Rental(self.regular_movie, 1)
		self.assertEqual(rental_regular.get_point(), 1.0)
		rental_regular = Rental(self.regular_movie, 5)
		self.assertEqual(rental_regular.get_point(), 1.0)

		rental_children = Rental(self.childrens_movie, 1)
		self.assertEqual(rental_children.get_point(), 1.0)
		rental_children = Rental(self.childrens_movie, 5)
		self.assertEqual(rental_children.get_point(), 1.0)
