
def correct_pass(user_pass):
    valid_pass = True
    if 3 <= len(user_pass) <= 16:
        if not ' ' in user_pass:
            for character in user_pass:
                if not (character.isalnum() or '-' in character or '_' in character):
                    valid_pass = False

            if valid_pass:
                print(user_pass)

user_inputs = input().split(', ')

for password in user_inputs:
    valid_user = correct_pass(password)
