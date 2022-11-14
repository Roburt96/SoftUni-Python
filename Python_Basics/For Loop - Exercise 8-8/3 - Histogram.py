p1 = 0 # Musala
p2 = 0 # Monblan
p3 = 0 # Kilimndjaro
p4 = 0 # K2
p5 = 0 # Everest
rows = int(input())

for i in range(rows):
    numbers = int(input())
    if numbers < 200:
        p1 += 1
    elif numbers < 400:
        p2 += 1
    elif numbers < 600:
        p3 += 1
    elif numbers < 800:
        p4 += 1
    else:
        p5 += 1
print(f"{p1 / rows * 100:.2f}%")
print(f"{p2 / rows * 100:.2f}%")
print(f"{p3 / rows * 100:.2f}%")
print(f"{p4 / rows * 100:.2f}%")
print(f"{p5 / rows * 100:.2f}%")
