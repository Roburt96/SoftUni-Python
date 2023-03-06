from project.movie import Movie
from unittest import TestCase, main

class TestMovie(TestCase):

    def setUp(self):
        self.movie = Movie('Thor', 2020, 10.0)

    def test_successfully_initialized(self):
        self.assertEqual('Thor', self.movie.name)
        self.assertEqual(2020, self.movie.year)
        self.assertEqual(10.0, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_movie_name_is_not_empty_string(self):
        message = "Name cannot be an empty string!"

        with self.assertRaises(ValueError) as ve:
            self.movie.name = ''
        self.assertEqual(message, str(ve.exception))

    def test_movie_name_is_valid(self):
        self.movie.name = 'Bai Ivan'
        self.assertEqual('Bai Ivan', self.movie.name)

    def test_movie_year_is_not_valid(self):
        message = 'Year is not valid!'
        with self.assertRaises(ValueError) as ve:
            self.movie.year = 1880
        self.assertEqual(message, str(ve.exception))

    def test_movie_year_is_valid(self):
        self.movie.year = 2000
        self.assertEqual(2000, self.movie.year)

    def test_add_actor_in_movie_actors_list(self):
        self.movie.actors = []
        self.movie.add_actor('Bai Ivan')
        self.assertEqual(1, len(self.movie.actors))
        self.assertEqual('Bai Ivan', self.movie.actors[0])

    def test_actor_already_added_in_movie_actors_list(self):
        self.movie.actors = ['Bai Ivan']
        expected = self.movie.add_actor('Bai Ivan')
        message = "Bai Ivan is already added in the list of actors!"
        self.assertEqual(message, expected)

    def test_main_movie_greater_than_other_movie(self):
        other = self.other_movie = Movie('Hulk', 2020, 8.0)
        result = self.movie > other
        message = '"Thor" is better than "Hulk"'
        self.assertTrue(self.movie.rating > other.rating)
        self.assertEqual(message, result)

    def test_other_movie_greater_than_main_movie(self):
        other = self.other_movie = Movie('Hulk', 2020, 12.0)
        result = self.movie < other
        message = '"Hulk" is better than "Thor"'
        self.assertTrue(other.rating > self.movie.rating)
        self.assertEqual(message, result)

    def test_repr_method(self):
        self.movie.add_actor('Bai Ivan')
        message = "Name: Thor\n" \
                  "Year of Release: 2020\n" \
                  "Rating: 10.00\n" \
                  "Cast: Bai Ivan"
        self.assertEqual(message, self.movie.__repr__())