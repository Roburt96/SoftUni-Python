world_record = float(input())
distance_in_meters = float(input())
time_for_one_meter = float(input())

resistance = ((distance_in_meters // 15) * 12.5)
total_time = distance_in_meters * time_for_one_meter + resistance

if total_time < world_record:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {total_time - world_record:.2f} seconds slower.")