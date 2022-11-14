numbers = input().split(", ")


def polidrome(num):
    for n in numbers:
        if n == n[::-1]:
            print("True")
        else:
            print("False")


polidrome(numbers)

