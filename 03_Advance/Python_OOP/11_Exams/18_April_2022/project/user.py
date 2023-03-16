from project.validator.validator import Validator
class User:

    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked = []
        self.movies_owned = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        Validator.user_check_empty_string_raise_error(value)
        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        Validator.user_check_age_under_6(value)
        self.__age = value

    def __str__(self):
        result = [f"Username: {self.username}, Age: {self.age}", "Liked movies:"]
        if self.movies_liked:
            [result.append(mov.details()) for mov in self.movies_liked]
        else:
            result.append("No movies liked.")
        result.append("Owned movies:")
        if self.movies_owned:
            [result.append(mov.details()) for mov in self.movies_owned]
        else:
            result.append("No movies owned.")
        return "\n".join(result)