

mackerel = float(input())
sprat = float(input())
palamud = float(input())
saffrite = float(input())
midi = int(input())

price_palamud = mackerel + mackerel * 0.60
total_palamud = palamud * price_palamud

price_saffrite = sprat + sprat * 0.80
total_saffrite = saffrite * price_saffrite
price_midi = midi * 7.50

price_for_all = total_palamud + total_saffrite + price_midi
print(f"{price_for_all: .2f}")