# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.

from rental import Rental
from customer import Customer
from movie_catalog import MovieCatalog

def make_movies():
    catalog = MovieCatalog()
    movies = [
        catalog.get_movie("Mulan"),
        # catalog.get_movie("The Irishman"),
        # catalog.get_movie("CitizenFour"),
        # catalog.get_movie("Frozen"),
        # catalog.get_movie("El Camino"),
        catalog.get_movie("Particle Fever"),
    ]
    return movies


if __name__ == '__main__':
    # Create a customer with some rentals
    customer = Customer("Edward Snowden")
    days = 1
    for movie in make_movies():
        customer.add_rental(Rental(movie, days))
        days += 1
    print(customer.statement())
