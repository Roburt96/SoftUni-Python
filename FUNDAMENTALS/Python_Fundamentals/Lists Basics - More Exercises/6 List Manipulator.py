numbers = [int(i) for i in input().split(" ")]
# slip_numbers = numbers[2:] + numbers[:2]
command = input().split()
while command != "End":

    if command[0] == "exchange":
        if 0 <= int(command[1]) <= len(numbers):
            numbers = numbers[int(command[1]) + 1:] + numbers[:int(command[1]) + 1]
        else:
            print("Invalid index")




