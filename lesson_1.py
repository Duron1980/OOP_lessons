from typing import Union


class Product():
    def __init__(self, name: str, price: float):
        self.name = str(name)
        self.price = float(price)

    def calculate_cost(self, quantity: Union[int, float]):
        return round(quantity * self.price, 2)


class Shopping_Cart():
    def __init__(self, another_cart=False):
        self.products: List[Product] = []
        self.quantities: List[Union[int, float]] = []
        self.obj = another_cart

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
        if not self.obj:
            return float(total)
        else:
            total = total + self.obj.show_total_cost()
            return float(total)


def main():
    cheeze = Product('Cheeze', 10)
    apple = Product('Apple', 50)
    cart1 = Shopping_Cart()
    cart1.add_to_cart(cheeze, 3)
    cart1.add_to_cart(cheeze, 4)
    cart2 = Shopping_Cart(cart1)
    cart2.add_to_cart(apple, 5)
    cart2.add_to_cart(apple, 10)
    print(cart1.show_total_cost())
    print(cart2.show_total_cost())


if __name__ == '__main__':
    main()
