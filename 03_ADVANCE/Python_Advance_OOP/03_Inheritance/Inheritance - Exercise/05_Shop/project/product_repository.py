
from project.product import Product


class ProductRepository:
    products = []

    def add(self, product: Product):
        self.products.append(product)


    def find(self, product: Product):
        for prod in self.products:
            if prod.__class__.__name__ == product.__class__.__name__:
                return prod

    def remove(self, product_name: str):
        for pos, prod in enumerate(self.products):
            if prod.name == product_name:
                del self.products[pos]

    def __repr__(self):
        result = ""
        for prod in self.products:
            if prod.name not in result:
                result += f"{prod.name}: {prod.quantity}\n"
        return result.rstrip()
