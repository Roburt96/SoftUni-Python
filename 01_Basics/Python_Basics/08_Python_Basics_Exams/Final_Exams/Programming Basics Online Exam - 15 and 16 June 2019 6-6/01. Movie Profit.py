movie = input()
days = int(input())
tickets = int(input())
price_tickets = float(input())
percent_cinema = int(input())

tickets_price = tickets * price_tickets
total_income = days * tickets_price
cinema_percent = total_income * percent_cinema / 100
movie_income = total_income - cinema_percent
print(f"The profit from the movie {movie} is {movie_income:.2f} lv.")

