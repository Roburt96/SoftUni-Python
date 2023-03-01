from collections import deque
pumps = int(input())
gas_stations = deque([int(x) for x in input().split()] for i in range(pumps))

for i in range(pumps):
    all_gas_stations = True
    gas_inside = 0
    for gas, distance in gas_stations:
        gas_inside += gas
        if distance > gas_inside:
            all_gas_stations = False
            break
        else:
            gas_inside -= distance

    if all_gas_stations:
        print(i)
        break
    else:
        gas_stations.append(gas_stations.popleft())





