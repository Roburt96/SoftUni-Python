
def add_(add_people):
    train[-1] += add_people


def insert_(insert_index, insert_people):
    train[insert_index] += insert_people


def leave_(leave_index, leave_people):
    train[leave_index] -= leave_people


wagons = int(input())
train = list()

for n in range(wagons):
    train.append(0)

command = input()
while command != "End":
    command, *data = command.split()

    if "add" in command:
        people = int(data[0])
        add_(people)
    elif "insert" in command:
        insert_index = int(data[0])
        insert_people = int(data[1])
        insert_(insert_index, insert_people)
    elif "leave" in command:
        leave_index = int(data[0])
        leave_people = int(data[1])
        leave_(leave_index, leave_people)
    command = input()


print(train)




