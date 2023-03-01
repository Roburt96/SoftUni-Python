class Shop:

    def __init__(self, *args):
        self.name = args[0]
        self.items = [x for x in args[1]]


    def get_items_count(self):
        return len(self.items)

shop = Shop("My Shop", ["Apples", "Bananas", "Cucumbers"])
print(shop.get_items_count())