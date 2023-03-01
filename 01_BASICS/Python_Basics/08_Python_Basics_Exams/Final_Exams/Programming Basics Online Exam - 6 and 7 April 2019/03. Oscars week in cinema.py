movie_name = input()
kind_of_hall = input()
number_of_tickets = int(input())

price = 0

if movie_name == "A Star Is Born":
    if kind_of_hall == "normal":
        price = number_of_tickets * 7.50
    elif kind_of_hall == "luxury":
        price = number_of_tickets * 10.50
    elif kind_of_hall == "ultra luxury":
        price = number_of_tickets * 13.50

if movie_name == "Bohemian Rhapsody":
    if kind_of_hall == "normal":
        price = number_of_tickets * 7.35
    elif kind_of_hall == "luxury":
        price = number_of_tickets * 9.45
    elif kind_of_hall == "ultra luxury":
        price = number_of_tickets * 12.75

if movie_name == "Green Book":
    if kind_of_hall == "normal":
        price = number_of_tickets * 8.15
    elif kind_of_hall == "luxury":
        price = number_of_tickets * 10.25
    elif kind_of_hall == "ultra luxury":
        price = number_of_tickets * 13.25

if movie_name == "The Favourite":
    if kind_of_hall == "normal":
        price = number_of_tickets * 8.75
    elif kind_of_hall == "luxury":
        price = number_of_tickets * 11.55
    elif kind_of_hall == "ultra luxury":
        price = number_of_tickets * 13.95

print(f"{movie_name} -> {price:.2f} lv.")
