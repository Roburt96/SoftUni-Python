class Inventory:
    def __init__(self, _capacity: int):
        self.start_capacity = _capacity
        self._capacity = _capacity
        self.items = []

    def add_item(self, item: str):
        if self._capacity - 1 >= 0:
            self.items.append(item)
            self._capacity -= 1
        else:
            return "not enough room in the inventory"

    def get_capacity(self):
        return self.start_capacity

    def __repr__(self):
        item = ', '.join(self.items)
        return f"Items: {item}.\nCapacity left: {self._capacity}"

inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)


