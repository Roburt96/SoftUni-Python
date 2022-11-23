first_player = input()
second_player = input()

first_player_point = 0
second_player_point = 0

command = input()
while command != "End of game":
    card_p_one = int(command)
    card_p_two = int(input())

    if card_p_one > card_p_two:
        first_player_point += abs(card_p_one - card_p_two)

    if card_p_two > card_p_one:
        second_player_point += abs(card_p_two - card_p_one)

    if card_p_one == card_p_two:
        print("Number wars!")
        card_p_one = int(input())
        card_p_two = int(input())

        if card_p_one > card_p_two:
            print(f"{first_player} is winner with {first_player_point} points")
            break
        if card_p_two > card_p_one:
            print(f"{second_player} is winner with {second_player_point} points")
            break

    command = input()

if command == "End of game":
    print(f"{first_player} has {first_player_point} points")
    print(f"{second_player} has {second_player_point} points")
