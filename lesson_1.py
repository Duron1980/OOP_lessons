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


class Shopping_Cart():
    def __init__(self):
        self.products: List[Product] = []
        self.quantities: List[Union[int, float]] = []

    def add_to_cart(self, product: Product, quantity: Union[int, float]):
        if product not in self.products:
            self.products.append(product)
            self.quantities.append(quantity)
        else:
            self.quantities[self.products.index(product)] += quantity

    def show_total_cost(self):
        total = 0
        for product, quantity in zip(self.products, self.quantities):
            total += product.calculate_cost(quantity)
            print(f'Product in cart now is {str(product)}, quantity is {quantity}')
        return total

    def add_cart_to_cart(self, another_cart):
        base_cart = {}
        append_cart = {}
        for product, quantity in zip(self.products, self.quantities):
            base_cart[product] = quantity
        for product, quantity in zip(another_cart.products, another_cart.quantities):
            append_cart[product] = quantity
        for product in append_cart:
            if product in base_cart:
                base_cart[product] += append_cart[product]
            else:
                base_cart[product] = append_cart[product]
        self.products = []
        self.quantities = []
        for value in base_cart:
            self.products.append(value)
            self.quantities.append(base_cart[value])


def main():
    cheeze = Product('Cheeze', 10.3)
    apple = Product('Apple', 50)
    meet = Product('Meet', 200)
    cart1 = Shopping_Cart()
    cart2 = Shopping_Cart()
    cart3 = Shopping_Cart()
    print('Cart1')
    cart1.add_to_cart(cheeze, 3)
    cart1.add_to_cart(apple, 4)
    print(f'Total cost in cart1 is {cart1.show_total_cost()}')
    print('_____________________________________________________________')
    print('Cart2')
    cart2.add_to_cart(meet, 2)
    cart2.add_to_cart(apple, 2)
    print(f'Total cost in cart2 is {cart2.show_total_cost()}')
    print('_____________________________________________________________')
    print('Cart3')
    cart3.add_to_cart(meet, 1)
    print(f'Total cost in cart3 is {cart3.show_total_cost()}')
    print('_____________________________________________________________')
    print("Add cart2 to cart1")
    cart1.add_cart_to_cart(cart2)
    print(f'Total cost in cart1 is {cart1.show_total_cost()}')
    print('_____________________________________________________________')
    print("Add cart3 to cart1")
    cart1.add_cart_to_cart(cart3)
    print(f'Total cost in cart1 is {cart1.show_total_cost()}')


if __name__ == '__main__':
    main()
