import sys

'''
Problem:
You have a function with too much responsabilities.
'''
def price_total(price, qtd, zip_code):
    total = price * qtd;
    
    # tax calc
    if total > 5:
        total = total + (total * 0.25);
    else:
        total = total + (total * 0.05);
    
    # calc delivery price
    if len(zip_code) > 3:
        total += 105;
    else:
        total += 65;

    return "Order total: {}".format(total);

'''
Solution:
Extract the responsabilities to other methods.
Give to the new methods names that describes what they do.
'''
def purchase_value(price, qtd):
    return price * qtd;

def calc_tax(price):
    if price > 5:
        price = price + (price * 0.25);
    else:
        price = price + (price * 0.05);
    
    return price;

def calc_delivery(price, zip_code):
    if len(zip_code) > 3:
        price += 105;
    else:
        price += 65;
    
    return price;

def right_price_total(price, qtd, zip_code):
    price = purchase_value(price, qtd);
    price = calc_tax(price);
    price = calc_delivery(price, zip_code);
    return "Order total: {}".format(price);

try:
    price = int(sys.argv[1]);
    qtd = int(sys.argv[2]);
    zip_code = sys.argv[3];
    result = right_price_total(price, qtd, zip_code);
    print(result);
except Exception:
    print("Please, inform the price, qtd and zip code.");