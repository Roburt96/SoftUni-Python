class Validator:

    #user
    @staticmethod
    def user_check_empty_string_raise_error(value):
        if value == "":
            raise ValueError("Invalid username!")

    @staticmethod
    def user_check_age_under_6(value):
        if value < 6:
            raise ValueError("Users under the age of 6 are not allowed!")

    #movie
    @staticmethod
    def movie_check_empty_string_raise_error(value):
        if value == '':
            raise ValueError("The title cannot be empty string!")

    @staticmethod
    def movie_check_year_raise_error(value):
        if value < 1888:
            raise ValueError("Movies weren't made before 1888!")

    @staticmethod
    def check_movie_owner(value):
        if value.__class__.__name__ != "User":
            raise ValueError("The owner must be an object of type User!")

    @staticmethod
    def movie_age_restriction(age, movie_class):
        if movie_class._age_restriction > age:
            raise ValueError(
                f"{movie_class.__class__.__name__} movies must be restricted for "
                f"audience under {movie_class._age_restriction} years!")

    #movie app
    @staticmethod
    def app_check_user_already_in_list(name, user_list):
        if any(user.username == name for user in user_list):
            raise ValueError("User already exists!")

    @staticmethod
    def app_check_user_not_registered_in_app(name, user_list):
        if all(name != user.username for user in user_list):
            raise Exception("This user does not exist!")

    @staticmethod
    def app_check_for_owner_movie(client_class, movie_class):
        if movie_class.owner.username != client_class.username:
            raise Exception(f"{client_class.username} is not the owner of the movie {movie_class.title}!")

    @staticmethod
    def app_upload_movie(movie_class, movie_list):
        if movie_class in movie_list:
            raise Exception("Movie already added to the collection!")

    @staticmethod
    def app_movie_not_uploaded(movie_class, movie_list):
        if movie_class not in movie_list:
            return Exception(f"The movie {movie_class.title} is not uploaded!")

    @staticmethod
    def app_user_cant_like_same_movie(user_class, movie_class):
        if movie_class in user_class.movies_liked:
            raise Exception(f"{user_class.username} already liked the movie {movie_class.title}!")

    @staticmethod
    def app_user_validate_own_movie(user_class, movie_class):
        if movie_class in user_class.movies_owned:
            raise Exception(f"{user_class.username} is the owner of the movie {movie_class.title}!")

    @staticmethod
    def app_user_dislike(user_class, movie_class):
        if movie_class not in user_class.movies_liked:
            raise Exception(f"{user_class.username} has not liked the movie {movie_class.title}!")
