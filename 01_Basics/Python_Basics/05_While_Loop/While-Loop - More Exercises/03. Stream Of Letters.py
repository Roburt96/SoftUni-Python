next_char = input()

final_string = ""
is_c_encountered = False
is_o_encountered = False
is_n_encountered = False

while next_char != "End":
    if next_char == "c":
        if is_c_encountered:
            final_string += next_char
        else:
            is_c_encountered = True
    elif next_char == "o":
        if is_o_encountered:
            final_string += next_char
        else:
            is_o_encountered = True
    elif next_char == "n":
        if is_n_encountered:
            final_string += next_char
        else:
            is_n_encountered = True
    elif next_char.isalpha():
        final_string += next_char

    if is_c_encountered and is_o_encountered and is_n_encountered:
        final_string += " "
        is_c_encountered = False
        is_o_encountered = False
        is_n_encountered = False
        print(final_string, end="")
    next_char = input()

print(final_string)
