# Пилешко меню 10.35
# Меню с риба 12.40
# Вегетарианско меню 8.15
# десерт 20 % от общата сума
# доставка 2.50

amount_of_chicken_menu = int(input())
amount_of_fish_menu = int(input())
amount_of_vegan_menu = int(input())
chicken_menu = 10.35
fish_menu = 12.40
vegan_menu = 8.15
delivery = 2.50

price_for_chicken_menu = amount_of_chicken_menu * chicken_menu
price_for_fish_menu = amount_of_fish_menu * fish_menu
price_for_vegan_menu = amount_of_vegan_menu * vegan_menu
price_for_all_menus = price_for_vegan_menu + price_for_chicken_menu + price_for_fish_menu
dessert = price_for_all_menus * 0.20

total_price_for_all = dessert+ price_for_all_menus  + delivery
print(float(total_price_for_all))