from typing import Union


class Product():
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def calculate_cost(self, quantity: Union[int, float]):
        return round(quantity * self.price, 2)

    def __str__(self):
        return self.name

    def __float__(self):
        return self.price

    def __repr__(self):
        return f'class-{self.__class__}, product name - {self.name}, price - {self.price}'


class Shopping_Cart():
    def __init__(self):
        self.products: List[Product] = []
        self.quantities: List[Union[int, float]] = []

    def add_to_cart(self, product: Product, quantity: Union[int, float]):
        if product not in self.products:
            self.products.append(product)
            self.quantities.append(quantity)
        else:
            idx = self.products.index(product)
            self.quantities[idx] += quantity

    def show_total_cost(self):
        total = 0
        for product, quantity in zip(self.products, self.quantities):
            total += product.calculate_cost(quantity)
            print(f'Product in cart now is {str(product)}, quantity is {quantity}')
        return total

    def __add__(self, other):
        new_cart = Shopping_Cart()
        new_cart.products = self.products.copy()
        new_cart.quantities = self.quantities.copy()
        if isinstance(other, Product):
            new_cart.add_to_cart(other, 1)
        if isinstance(other, Shopping_Cart):
            if other == new_cart:
                new_cart.quantities = [quantity * 2 for quantity in new_cart.quantities]
                return new_cart
            for product, quantity in zip(other.products, other.quantities):
                new_cart.add_to_cart(product, quantity)
        return new_cart

    def __eq__(self, other):
        return set(self.products) == set(other.products) and set(self.quantities) == set(other.quantities)

def main():
    cheeze = Product('Cheeze', 10.3)
    apple = Product('Apple', 50)
    meet = Product('Meet', 200)
    cart1 = Shopping_Cart()
    cart2 = Shopping_Cart()
    print('Cart1')
    cart1.add_to_cart(cheeze, 3)
    cart1.add_to_cart(apple, 4)
    print(f'Total cost in cart1 is {cart1.show_total_cost()}')
    print('_____________________________________________________________')
    print('Cart2')
    cart2.add_to_cart(apple, 4)
    cart2.add_to_cart(cheeze, 3)
    print(f'Total cost in cart2 is {cart2.show_total_cost()}')
    print('_____________________________________________________________')
    New_cart = cart1 + cart2
    print(f'Total cost in New_cart is {New_cart.show_total_cost()}')
    print(cart1 == cart2)

if __name__ == '__main__':
    main()
