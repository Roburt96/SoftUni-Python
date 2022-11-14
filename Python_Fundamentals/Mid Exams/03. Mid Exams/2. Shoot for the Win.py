targets = [int(x) for x in input().split()]
shots = 0
command = input()


def reduce_increase_targets(index):
    global shots
    if targets[index] != -1:
        value = targets[index]
        targets[index] = -1
        shots += 1

        for shoot in range(len(targets)):
            if targets[shoot] != -1:
                if targets[shoot] > value:
                    targets[shoot] -= value
                else:
                    targets[shoot] += value


while command != "End":
    index_command = int(command)

    if 0 <= index_command < len(targets):
        reduce_increase_targets(index_command)

    command = input()


print(f"Shot targets: {shots} ->", *targets, sep=" ")
