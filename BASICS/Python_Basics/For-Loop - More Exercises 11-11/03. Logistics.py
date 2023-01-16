number_of_cargo = int(input())
all_cargo = 0
truck = 0
train = 0
bus = 0
cargo_price = 0
price_for_all = 0
average_price_cargo = 0



for cargo in range(number_of_cargo):
    current_cargo = int(input())
    if current_cargo <= 3:
        bus += current_cargo
    elif 4 <= current_cargo <= 11:
        truck += current_cargo
    elif current_cargo >= 12:
        train += current_cargo


all_cargo = bus + truck + train
price_for_all = bus * 200 + truck * 175 + train * 120
average_price_cargo = price_for_all / all_cargo

print(f"{average_price_cargo:.2f}")
print(f"{bus / all_cargo * 100:.2f}%")
print(f"{truck / all_cargo * 100:.2f}%")
print(f"{train / all_cargo * 100:.2f}%")
