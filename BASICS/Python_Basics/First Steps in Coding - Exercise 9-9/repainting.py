required_amount_of_nylon = int(input())
required_amont_of_dye = int(input())
amount_of_thinner = int(input())
hours_to_complete = int(input())

price_for_nylon = (required_amount_of_nylon + 2) * 1.50
price_for_dye = (required_amont_of_dye * 1.10) * 14.50
price_for_thinner = amount_of_thinner * 5
total_price = price_for_thinner + price_for_dye + price_for_nylon + 0.40
price_workers = total_price * 0.3 * hours_to_complete
total_price_for_complete = price_workers + total_price
print(total_price_for_complete)
