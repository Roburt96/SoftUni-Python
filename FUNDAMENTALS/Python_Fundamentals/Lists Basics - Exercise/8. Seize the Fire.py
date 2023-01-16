fire_cells = input().split("#")
water = int(input())
total_fire = 0
total_effort = 0
water_left = water
out_cells = []

for text in fire_cells:
    fire_type, cells_value = [int(x) if x.isdigit() else x for x in text.split(" = ")]
    if water_left >= cells_value:
        if any(["High" in fire_type and cells_value in range(81, 126),
                "Medium" in fire_type and cells_value in range(51, 80),
                "Low" in fire_type and cells_value in range(1, 50)]):
            out_cells.append(cells_value)
            total_fire += cells_value
            total_effort += cells_value * 0.25
            water_left -= cells_value

print("Cells:")
for n in out_cells:
    print(f" - {n}")
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")











