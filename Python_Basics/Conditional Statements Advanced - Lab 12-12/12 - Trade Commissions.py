city = input()
sales = float(input())

if city == "Sofia":
    if 0 <= sales <= 500:
        print(f"{sales * 0.05:.2f}")
    elif 500 <= sales <= 1000:
        print(f"{sales * 0.07:.2f}")
    elif 1000 <= sales <= 10000:
        print(f"{sales * 0.08:.2f}")
    elif sales > 10000:
        print(f"{sales * 0.12:.2f}")
    else:
        print("error")
elif city == "Varna":
    if 0 <= sales <= 500:
        print(f"{sales * 0.045:.2f}")
    elif 500 <= sales <= 1000:
        print(f"{sales * 0.075:.2f}")
    elif 1000 <= sales <= 10000:
        print(f"{sales * 0.10:.2f}")
    elif sales > 10000:
        print(f"{sales * 0.13:.2f}")
    else:
        print("error")
elif city == "Plovdiv":
    if 0 <= sales <= 500:
        print(f"{sales * 0.055:.2f}")
    elif 500 <= sales <= 1000:
        print(f"{sales * 0.08:.2f}")
    elif 1000 <= sales <= 10000:
        print(f"{sales * 0.12:.2f}")
    elif sales > 10000:
        print(f"{sales * 0.145:.2f}")
    else:
        print("error")
else:
    print("error")
