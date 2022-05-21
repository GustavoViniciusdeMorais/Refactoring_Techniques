import sys

'''
Problem:
You built a sequence of method calls to build
the parameters to a next method as follows.
'''

def get_seasonal_discount():
    return 5;

def get_fees():
    return 0.45;

def discounted_price(base_price, season_discount, fees):
    return (base_price - season_discount) + fees;


# The following code is the WRONG one.
quantity = 5; # fake value
itemPrice = 15; # fake value
base_price = quantity * itemPrice;
season_discount = get_seasonal_discount();
fees = get_fees();
final_price = discounted_price(base_price, season_discount, fees);


''' ----------------------------------------------
Solution:
Put the other methods calls inside the method that
before was receiving the methods results as parameters.
'''
def right_discounted_price(base_price):
    season_discount = get_seasonal_discount();
    fees = get_fees();
    return (base_price - season_discount) + fees;

try:
    # The following code is the RIGHT one.
    quantity = int(sys.argv[1]);
    itemPrice = int(sys.argv[2]);
    base_price = quantity * itemPrice;
    final_price = right_discounted_price(base_price);
    print("Right final price: {}".format(final_price));

except Exception:
    print("Pass some quantity value and some value to be the fake price.");