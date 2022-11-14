password = input()
char_in_range = False
letters_digit_only = False
two_digits = False
num_check = 0


def check_pass(check):
    global char_in_range, letters_digit_only, two_digits, num_check
    if 6 <= len(check) <= 10:
        char_in_range = True
    if check.isalnum():
        letters_digit_only = True
    for letter in check:
        if letter.isdigit():
            num_check += 1
        if num_check == 2:
            two_digits = True
            break


check_pass(password)

if all([char_in_range, letters_digit_only, two_digits]):
    print("Password is valid")
if not char_in_range:
    print("Password must be between 6 and 10 characters")
if not letters_digit_only:
    print("Password must consist only of letters and digits")
if not two_digits:
    print("Password must have at least 2 digits")


