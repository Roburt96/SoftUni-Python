def flights(*args):
    destination = {}
    for key in range(0, len(args) + 1, 2):
        desti = args[key]

        if desti == 'Finish':
            break
        value = int(args[key + 1])
        if desti in destination:
            destination[desti] += value
        else:
            destination[desti] = destination.get(desti, 0) + value

    return destination


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print()
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print()
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))