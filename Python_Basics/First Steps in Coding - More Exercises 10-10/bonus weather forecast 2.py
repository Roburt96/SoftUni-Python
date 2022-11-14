weather = float(input())

if weather < 5:
    print("unknown")
elif weather <= 11.9:
    print("Cold")
elif weather <= 14.9:
    print("Cool")
elif weather <= 20:
    print("Mild")
elif weather <= 25.9:
    print("Warm")
elif weather <= 35:
    print("Hot")
else:
    print("unknown")
