
part_price = 0

command = input()

while command != "special" or command == "regular":

    if command == "special":
        break
    if command == "regular":
        break
    if float(command) < 0:
        print("Invalid price!")
    else:
        part_price += float(command)
    command = input()


total_taxes = part_price * 0.20
price_with_taxes = part_price + total_taxes


if command == "special":
    if part_price == 0:
        print("Invalid order!")
    else:
        discount_price = price_with_taxes - (price_with_taxes * 0.10)
        print(f"Congratulations you've just bought a new computer!")
        print(f"Price without taxes: {part_price:.2f}$")
        print(f"Taxes: {total_taxes:.2f}$")
        print("-----------")
        print(f"Total price: {discount_price:.2f}$")

if command == "regular":
    if part_price == 0:
        print("Invalid order!")
    else:
        print(f"Congratulations you've just bought a new computer!")
        print(f"Price without taxes: {part_price:.2f}$")
        print(f"Taxes: {total_taxes:.2f}$")
        print("-----------")
        print(f"Total price: {price_with_taxes:.2f}$")























# command = 0
# total = 0
# parts = True
#
#
# def buying_pc(off):
#     taxes = total * 0.20
#     global parts
#     if off:
#         final_price = (total + taxes) - (total + taxes) * 0.10
#     else:
#         final_price = total + taxes
#     parts = False
#     if total == 0:
#         print("Invalid order!")
#     else:
#         print("Congratulations you've just bought a new computer!")
#         print(f"Price without taxes: {total:.2f}$")
#         print(f"Taxes: {taxes:.2f}$")
#         print("-----------")
#         print(f"Total price: {final_price:.2f}$")
#
#
# while parts:
#     command = float(command)
#     if command >= 0:
#         total += command
#     else:
#         print("Invalid price!")
#     command = input()
#     if command == "special":
#         buying_pc(True)
#     elif command == "regular":
#         buying_pc(False)
