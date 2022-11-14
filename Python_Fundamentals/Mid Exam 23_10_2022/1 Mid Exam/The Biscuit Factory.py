import math
biscuits_produced_per_day = int(input())
workers_count = int(input())
competing_factory_produces = int(input())
total_biscuits = 0

for i in range(1, 30 + 1):
    if i % 3 == 0:
        worker_per_3th_day = workers_count * (biscuits_produced_per_day * 75 / 100)
        total_biscuits += math.floor(worker_per_3th_day)
    else:
        total_biscuits += workers_count * biscuits_produced_per_day


difference = total_biscuits - competing_factory_produces
percentage_production = abs((difference / competing_factory_produces) * 100)

print(f"You have produced {total_biscuits} biscuits for the past month.")
if total_biscuits > competing_factory_produces:
    print(f"You produce {percentage_production:.2f} percent more biscuits.")
else:
    print(f"You produce {percentage_production:.2f} percent less biscuits.")