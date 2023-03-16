from project.movie_specification.movie import Movie


class Action(Movie):
    _age_restriction = 12

    def __init__(self, name, year, owner, age_restriction=12):
        super().__init__(name, year, owner, age_restriction)