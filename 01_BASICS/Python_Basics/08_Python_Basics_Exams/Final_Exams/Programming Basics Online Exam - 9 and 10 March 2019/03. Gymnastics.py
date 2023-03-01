country = input()
appliance = input()
diff = 0
performance = 0
total_point = 20

if country == "Russia":
    if appliance == "ribbon":
        diff += 9.100
        performance += 9.400
    elif appliance == "hoop":
        diff += 9.300
        performance += 9.800
    elif appliance == "rope":
        diff += 9.600
        performance += 9.000

if country == "Bulgaria":
    if appliance == "ribbon":
        diff += 9.600
        performance += 9.400
    elif appliance == "hoop":
        diff += 9.550
        performance += 9.750
    elif appliance == "rope":
        diff += 9.500
        performance += 9.400

if country == "Italy":
    if appliance == "ribbon":
        diff += 9.200
        performance += 9.500
    elif appliance == "hoop":
        diff += 9.450
        performance += 9.350
    elif appliance == "rope":
        diff += 9.700
        performance += 9.150

point = diff + performance
remaining = total_point - point
percent = (remaining / total_point) * 100

print(f"The team of {country} get {point:.3f} on {appliance}.")
print(f"{percent:.2f}%")
