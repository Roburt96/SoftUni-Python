import sys
numbers_of_movies = int(input())

highest_rating = -sys.maxsize
lowest_rating = sys.maxsize
average_rating = 0
rating = 0
best_movie = ""
worst_movie = ""

for movie in range(numbers_of_movies):
    movie_name = input()
    rating = float(input())
    if rating <= lowest_rating:
        worst_movie = movie_name
        lowest_rating = rating

    if rating >= highest_rating:
        best_movie = movie_name
        highest_rating = rating
    average_rating += rating

average_rating = average_rating / numbers_of_movies

print(f"{best_movie} is with highest rating: {highest_rating:.1f}")
print(f"{worst_movie} is with lowest rating: {lowest_rating:.1f}")
print(f"Average rating: {average_rating:.1f}")
