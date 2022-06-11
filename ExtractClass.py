import sys

'''
Problem:
A class has more responsabilities that it should
have.
'''
class WrongPerson(object):
    def __init__(self, name, office_area_code, office_number):
        self.name = name;
        self.office_area_code = office_area_code;
        self.office_number = office_number;
    def get_phone_number(self):
        return self.office_number;

'''
Solution:
Extract the fields and methods to proper classes
that represents those tasks to be done.
'''
class PhoneNumber(object):
    def __init__(self, office_area_code, office_number):
        self.office_area_code = office_area_code;
        self.office_number = office_number;
    def get_phone_number(self):
        return "{} {}".format(self.office_area_code, self.office_number);

class Person(object):
    def __init__(self, name, phone_number):
        self.name = name;
        self.phone_number = phone_number;
    def get_phone_number(self):
        return self.phone_number.get_phone_number();

try:
    office_area_code = sys.argv[1];
    office_number = sys.argv[2];
    phone_number = PhoneNumber(office_area_code, office_number);
    person = Person('Gustavo', phone_number);
    print(person.get_phone_number());
except Exception as e:
    print(e);