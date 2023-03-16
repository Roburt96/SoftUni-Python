from project.movie_specification.movie import Movie
from project.user import User
from project.validator.validator import Validator


class MovieApp:

    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def __find_username(self, username):
        for u in self.users_collection:
            if u.username == username:
                return u

    def register_user(self, username: str, age: int):
        Validator.app_check_user_already_in_list(username, self.users_collection)
        self.users_collection.append(User(username, age))
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        Validator.app_check_user_not_registered_in_app(username, self.users_collection)
        user = self.__find_username(username)
        Validator.app_check_for_owner_movie(user, movie)
        Validator.app_upload_movie(movie, self.movies_collection)

        self.movies_collection.append(movie)
        user.movies_owned.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        user = self.__find_username(username)
        Validator.app_check_for_owner_movie(user, movie)
        Validator.app_movie_not_uploaded(movie, self.movies_collection)

        for key, value in kwargs.items():
            if key == 'title':
                movie.title = value
            elif key == 'year':
                movie.year = value
            elif key == 'age_restriction':
                movie.age_restriction = value

        return f"{username} successfully edited {movie.title} movie."


    def delete_movie(self, username: str, movie: Movie):
        user = self.__find_username(username)
        Validator.app_check_for_owner_movie(user, movie)
        Validator.app_movie_not_uploaded(movie, self.movies_collection)

        title_movie = movie.title
        self.movies_collection.remove(movie)
        user.movies_owned.remove(movie)
        return f"{username} successfully deleted {title_movie} movie."

    def like_movie(self, username: str, movie: Movie):
        user = self.__find_username(username)
        Validator.app_user_cant_like_same_movie(user, movie)
        Validator.app_user_validate_own_movie(user, movie)

        movie.likes += 1
        user.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = self.__find_username(username)
        Validator.app_user_dislike(user, movie)

        movie.likes -= 1
        user.movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."


    def display_movies(self):
        if not self.movies_collection:
            return "No movies found."

        return '\n'.join(s.details() for s in sorted(self.movies_collection, key=lambda x: (-x.year, x.title)))

    def __str__(self):
        result = ["All users: "]
        if not self.users_collection:
            result[0] += "No users."
        else:
            result[0] += ', '.join(u.username for u in self.users_collection)

        result.append("All movies: ")
        if not self.movies_collection:
            result[1] += "No movies."
        else:
            result[1] += ', '.join(u.title for u in self.movies_collection)

        return "\n".join(result)




