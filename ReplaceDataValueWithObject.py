import sys

'''
Use this technique when a class has data fields
that contains behaviours by themselves and data
related.
'''

'''
Problem:
The order class has an attirubte that have behavior
on its own and other data related.
'''
class Order(object):
    customer_name = '';
    customer_address = '';

    def __init__(self, customer_name, customer_address):
        self.customer_address = customer_address;
        self.customer_name = customer_name;

    def get_customer_address(self):
        return self.customer_address;

'''
Solution:
Extract the customer data and its behavior to
an appropriate class
'''
class Customer(object):
    name = '';
    address = '';

    def __init__(self, name, address):
        self.name = name;
        self.address = address;
    
    def get_address(self):
        return self.address;
    
    def get_name(self):
        return self.name;
        
class NewOrder(object):

    def __init__(self, customer):
        self.customer = customer;

    def get_customer_address(self):
        return self.customer.get_address();
    
    def get_customer_name(self):
        return self.customer.get_name();

try:
    name = sys.argv[1];
    address = sys.argv[2];
    customer = Customer(name, address);
    order = NewOrder(customer);
    print("Customer {} has the address: {}".format(order.get_customer_name(), 
        order.get_customer_address()));
except Exception:
    print("Please inform the name and address of a fake customer.");