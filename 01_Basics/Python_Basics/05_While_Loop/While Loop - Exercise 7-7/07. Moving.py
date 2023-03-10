width = int(input())
length = int(input())
height = int(input())

total_carton = 0
free_space = width * length * height

command = input()
while command != "Done":
    carton = int(command)
    total_carton += carton

    if total_carton > free_space:
        print(f"No more free space! You need {abs(total_carton - free_space)} Cubic meters more.")
        break

    command = input()

if free_space > total_carton:
    print(f"{free_space - total_carton} Cubic meters left.")
