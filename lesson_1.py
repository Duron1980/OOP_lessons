"""
Challenge:

#. Implement ``Product`` class
#. Each ``Product`` instance should implement properties:
    * ``name`` - a product's name, like apple, cheese etc.
    * ``price`` - a price for a single unit
#. ``Product`` instance should have a behavior of calculating total
   price for a specified quantity of goods
#. Implement ``ShoppingCart`` class
#. ``ShoppingCart`` instance should combine products instances and
    corresponding purchased quantities.
#. ``ShoppingCart`` instance should implement a method to calculate
   the total price of entire cart.

"""
import random
from typing import Union


class Product():
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price

    def calculate_cost(self, quantity: Union[int, float]):
        return round(quantity * self.price, 2)


class Shopping_Cart():
    def __init__(self):
        self.products: List[Product] = []
        self.quantities: List[Union[int, float]] = []

    def putin_products(self, product: Product, quantity: Union[int, float]):
        self.products.append(product)
        self.quantities.append(quantity)

    def show_total_cost(self):
        total = 0
        for product, quantity in zip(self.products, self.quantities):
            total += product.calculate_cost(quantity)
        return total


def main():
    # goods = ['Cheese', 'Apple', 'Butter', 'Meat']
    Cheese = Product('Chheae', 350)
    Apple = Product('Apple', 42)
    Meet = Product('Meet', 200)
    cart = Shopping_Cart()
    cart.putin_products(Cheese, 2)
    cart.putin_products(Apple, 1.5)
    cart.putin_products(Meet, 2.5)
    print(cart.show_total_cost())


if __name__ == '__main__':
    main()
