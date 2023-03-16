from abc import ABC, abstractmethod

from project.validator.validator import Validator


class Movie(ABC):

    @abstractmethod
    def __init__(self, title: str, year: int, owner: object, age_restriction: int):
        self.title = title
        self.year = year
        self.owner = owner
        self.age_restriction = age_restriction
        self.likes = 0

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        Validator.movie_check_empty_string_raise_error(value)
        self.__title = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        Validator.movie_check_year_raise_error(value)
        self.__year = value

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        Validator.check_movie_owner(value)
        self.__owner = value

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        Validator.movie_age_restriction(value, self)
        self.__age_restriction = value

    def details(self):
        result = f"{self.__class__.__name__} - Title:{self.title}, " \
                 f"Year:{self.year}, Age restriction:{self.age_restriction}, " \
                 f"Likes:{self.likes}, Owned by:{self.owner.username}"
        return result



