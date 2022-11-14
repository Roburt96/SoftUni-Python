days = int(input())
plunder_for_day = int(input())
expected_plunder = int(input())
total_plunder = 0

for i in range(1, days + 1):
    total_plunder += plunder_for_day
    if i % 3 == 0:
        total_plunder += plunder_for_day * 0.50
    if i % 5 == 0:
        total_plunder -= total_plunder * 0.30

if total_plunder >= expected_plunder:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
else:
    percent = (total_plunder * 100) / expected_plunder
    print(f"Collected only {percent:.2f}% of the plunder.")
