class Storage:

    def __init__(self, capacity):     # -----> Storage(4) -> max 4
        self.capacity = capacity    # ----> 4
        self.storage = []

    def add_product(self, product: str):
        if self.capacity - 1 >= 0:
            self.storage.append(product)
            self.capacity -= 1

    def get_products(self):
        return self.storage


storage = Storage(4)
storage.add_product("apple")
storage.add_product("banana")
storage.add_product("potato")
storage.add_product("tomato")
storage.add_product("bread")

print(storage.get_products())
