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
class Employee(object):
    def __init__(self, employee_type):
        self.employee_type = employee_type;
    
    def get_job_title(self):
        return self.employee_type.job_title();
    
    def get_payment(self):
        return self.employee_type.get_payment();

class EmployeeType():
    def job_title(self):
        pass

    def get_payment(self):
        pass

class Engineer(EmployeeType):
    def job_title(self):
        return 'Engineer';
    
    def get_payment(self):
        return 2500;

class SalesMan(EmployeeType):
    def job_title(self):
        return 'Sales Man';
    
    def get_payment(self):
        return 3200;

try:
    type = int(sys.argv[1]);
    employee_type = '';
    result = '';
    name = '';
    if type == 1:
        employee_type = Engineer();
    elif type == 2:
        employee_type = SalesMan();
    
    employee = Employee(employee_type);
    result = employee.get_payment();
    name = employee.get_job_title();

    print("Payment to the {} is {}.".format(name, result));

except Exception:
    print("Insert a number [1, 2] as parameter.");