import sys

'''
Problem:
Here we have an expression inside a function.
The expression is calculating the base price.
'''
def calculate_total(quantity, item_price):
    base_price = quantity * item_price;
    if base_price > 1000:
        return base_price * 0.95;
    else:
        return base_price * 0.98;

'''
Solution:
Extract the expression into a method.
'''
def base_price(quantity, item_price):
    return quantity * item_price;

def solution_calculate_total(quantity, item_price):
    if base_price(quantity, item_price) > 1000:
        return base_price(quantity, item_price) * 0.95;
    else:
        return base_price(quantity, item_price) * 0.98;
try:
    quantity = int(sys.argv[1]);
    item_price = int(sys.argv[2]);
    result = solution_calculate_total(quantity, item_price);
    print("Purchase ammount is: {}".format(result))
except Exception:
    print("You should pass two arguments to this script")