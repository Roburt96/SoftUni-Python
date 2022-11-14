# vegetables N
# fruits M

Nkg = float(input())
Mkg = float(input())
totalN = int(input())
totalM = int(input())

priceN = Nkg * totalN
priceM = Mkg * totalM
total = (priceN + priceM) / 1.94
print(f"{total: .2f}")