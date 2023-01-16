# a = int(input())
# b = int(input())
#
# new_a = b
# new_b = a
#
# print("Before:")
# print(f"a = {a}")
# print(f"b = {b}")
# print("After:")
# print(f"a = {new_a}")
# print(f"b = {new_b}")


def change_numbers(num1, num2):
    new_num_one = num2
    new_num_two = num1
    return f"Before: \n" \
           f"num_one = {num1} \n" \
           f"num_two = {num2} \n" \
           f"After: \n" \
           f"num_one = {new_num_one} \n" \
           f"num_twp = {new_num_two}"


num_one, num_two = int(input()), int(input())
print(change_numbers(num_one, num_two))