junior_bikers = int(input())
seniors_bikers = int(input())
route_type = input()

price = 0
discount = 0

if route_type == "trail":
    price = (junior_bikers * 5.50) + (seniors_bikers * 7)
elif route_type == "cross-country":
    price = (junior_bikers * 8) + (seniors_bikers * 9.50)
    if junior_bikers + seniors_bikers >= 50:
        discount = ((junior_bikers * 8) + (seniors_bikers * 9.50)) * 0.25
        price = ((junior_bikers * 8) + (seniors_bikers * 9.50)) - discount
elif route_type == "downhill":
    price = (junior_bikers * 12.25) + (seniors_bikers * 13.75)
elif route_type == "road":
    price = (junior_bikers * 20) + (seniors_bikers * 21.50)

donation = price * 0.05
final_sum = price - donation

print(f"{final_sum:.2f}")
