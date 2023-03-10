text = input()
symbols = {}
for sym in text:
    if sym not in symbols:
        symbols[sym] = 1
    else:
        symbols[sym] += 1

for key, value in sorted(symbols.items(), key=lambda x: x[0]):
    print(f"{key}: {value} time/s")
