control_min = int(input())
control_sec = int(input())
metric = float(input())
sec_100m = int(input())

control_time = control_min * 60 + control_sec
reduction = metric / 120
total_reduction = reduction * 2.5
total_time = (metric / 100) * sec_100m - total_reduction
time = abs(control_time - total_time)

if control_time < total_time:
    print(f"No, Marin failed! He was {time:.3f} second slower.")
elif control_time > total_time:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {total_time:.3f}.")
