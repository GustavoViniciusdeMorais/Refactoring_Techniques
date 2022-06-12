import sys

'''
Problem:
A class has features that are used just
on certain cases.
'''
class WrongJobItem(object):
    def __init__(self, total_price, unit_price, employee):
        self.total_price = total_price;
        self.unit_price = unit_price;
        self.employee = employee;
    def get_total_price(self):
        return self.total_price;
    def get_unit_price(self):
        return self.unit_price;
    def get_employee(self):
        return self.employee;

'''
Solution:
Create a subclass to use on the specific
cases.
'''
class JobItem(object):
    def __init__(self, total_price):
        self.total_price = total_price;
    def get_total_price(self):
        return self.total_price;

class LaborItem(JobItem):
    def __init__(self, total_price, unit_price, employee):
        self.total_price = total_price;
        self.unit_price = unit_price;
        self.employee = employee;
    def get_unit_price(self):
        return self.unit_price;
    def get_employee(self):
        return self.employee;

try:
    total_price = sys.argv[1];
    unit_price = sys.argv[2];
    employee = sys.argv[3];
    labor = LaborItem(total_price, unit_price, employee);
    print("The price is {} per {} units by the employee {}".format(
        labor.get_total_price(), labor.get_unit_price(), labor.get_employee()
    ));
except Exception as e:
    print(e);