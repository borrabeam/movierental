import unittest
from customer import Customer
from rental import Rental, PriceCode
from movie import Movie


class RentalTest(unittest.TestCase):
	
	def setUp(self):
		self.new_movie = Movie("Mulan", PriceCode.new_release)
		self.regular_movie = Movie("CitizenFour", PriceCode.normal)
		self.childrens_movie = Movie("Frozen", PriceCode.childrens)

	def test_movie_attributes(self):
		"""trivial test to catch refactoring errors or change in API of Movie"""
		m = Movie("CitizenFour", PriceCode.normal)
		self.assertEqual("CitizenFour", m.get_title())
		self.assertEqual(PriceCode.normal, m.get_price_code())

	
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
