import sys

'''
Problem:
A class have a method that runs out
of its responsabilities
'''
class WrongOrder(object):

    def __init__(self, base_price, qtd_products):
        self.base_price = base_price;
        self.qtd_products = qtd_products;

    def price(self):
        return self.base_price * self.qtd_products;

'''
Solution:
Extract the method to a new class
responsible for the rule.
'''
class PriceCalculator(object):
    def __init__(self, order):
        self.order = order;

    def compute(self):
        return self.order.base_price * self.order.qtd_products;

class Order(object):

    def __init__(self, base_price, qtd_products):
        self.base_price = base_price;
        self.qtd_products = qtd_products;

    def price(self):
        return PriceCalculator(self).compute();

try:
    base_price = int(sys.argv[1]);
    qtd_products = int(sys.argv[2]);
    order = Order(base_price, qtd_products);
    result = order.price();
    print("Result: {}".format(result));
except Exception as e:
    print(e);