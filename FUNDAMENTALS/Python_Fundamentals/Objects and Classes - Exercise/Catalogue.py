class Catalogue:

    def __init__(self, name):
        self.name = name
        self.products = []
        self.products_by_letter = []

    def add_product(self, product: str):
        self.products.append(product)

    def get_by_letter(self, alpha: str):
        return [product for product in self.products if product.startswith(alpha)]

    def __repr__(self):
        product_list = '\n'.join(sorted(self.products))
        return f"Items in the {self.name} catalogue:\n{product_list}"


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)