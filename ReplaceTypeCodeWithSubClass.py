import sys

'''
Problem:
A class have fields that describes what is the
type of the class.
'''
class WrongEmployee(object):
    def __init__(self, engineer, salesman):
        self.engineer = engineer;
        self.salesman = salesman;
    def get_payment(self):
        if self.engineer == 1:
            return 2500;
        elif self.salesman == 1:
            return 3200;

'''
Solution:
Build sublcasses of the class to represent
the types used to determine its behaviour.
'''
class Employee():
    def job_title(self):
        pass

    def get_payment(self):
        pass

class Engineer(Employee):
    def job_title(self):
        return 'Engineer';
    
    def get_payment(self):
        return 2500;

class SalesMan(Employee):
    def job_title(self):
        return 'Sales Man';
    
    def get_payment(self):
        return 3200;

try:
    type = int(sys.argv[1]);
    result = '';
    name = '';
    if type == 1:
        engineer = Engineer();
        result = engineer.get_payment();
        name = engineer.job_title();
    elif type == 2:
        salesman = SalesMan();
        result = salesman.get_payment();
        name = salesman.job_title();
    print("Payment to the {} is {}.".format(name, result));
except Exception:
    print("Insert a number [1, 2] as parameter.");