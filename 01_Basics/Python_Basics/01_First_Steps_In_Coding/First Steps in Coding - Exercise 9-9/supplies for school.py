number_of_pen_packs = int(input())
number_of_markers_packs = int(input())
liters_of_board_cleaner = int(input())
percent_discount = int(input())

pen_price = float(number_of_pen_packs * 5.80)
markers_price = float(number_of_markers_packs * 7.20)
board_cleaner_price = float(liters_of_board_cleaner * 1.20)
reduction = percent_discount / 100
total_price = float(pen_price + markers_price + board_cleaner_price)

discount = total_price * reduction
price = total_price - discount
print(f"{price:.2f} lv.")


