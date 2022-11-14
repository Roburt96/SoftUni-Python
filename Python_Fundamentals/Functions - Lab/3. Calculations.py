operation = input()
num1 = int(input())
num2 = int(input())


def solve(a, b, operation):
    result = None
    if operation == "multiply":
        result = a * b
    elif operation == "divide":
        result = int(a / b)
    elif operation == 'add':
        result = a + b
    elif operation == "subtract":
        result = a - b
    return result


print(solve(num1, num2, operation))



