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
from prettytable import PrettyTable

class Product():
    def __init__(self, name_product: str, product_quantities: float, price_product: int):
        self.name_product = name_product
        self.product_quantities = product_quantities
        self.price_product = price_product

    def calculate_cost(self):
        return round(self.product_quantities * self.price_product, 2)

class Shopping_Cart():
    def __init__(self, objs: list):
        self.cart = objs
        self.show_check()

    def show_check(self):
        sum = 0
        check = PrettyTable()
        check.field_names = ['Product name','Price per kg, grn:','Quantitie, kg:','Cost, grn:']
        for product in self.cart:
            check.add_row([product.name_product, product.price_product, product.product_quantities, product.calculate_cost()])
            sum = sum + product.calculate_cost()
        check.add_row(['','','TOTAL COST',sum])
        print(check)

def main():
    goods = ['Cheese', 'Apple', 'Butter', 'Meat']
    bag = [Product(value, product_quantities=round(random.uniform(1, 2), 2), price_product=random.randint(50, 300)) for value in goods]
    my_cart = Shopping_Cart(bag)

if __name__ == '__main__':
    main()

