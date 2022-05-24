class DaysTempRange(object):
    def __init__(self, low, high):
        self.low = low;
        self.high = high;
    def get_low(self):
        return self.low;
    def get_high(self):
        return self.high;

day_temp = DaysTempRange(12, 30);

class Plan(object):
    def with_range(self, low, high):
        return "Wrong: Temperature of the day will be between {} and {}".format(low, high);

plan = Plan();

'''
Problem:
You built a method that receives two or more parameters
from an object attributes.
'''
low = day_temp.get_low();
high = day_temp.get_high();
print(plan.with_range(low, high));

'''
Solution:
Use the whole object as the parameter to the function.
'''

class RightPlan(object):
    def with_range(self, temp: DaysTempRange):
        low = temp.get_low();
        high = temp.get_high();
        return "From Right: Temperature of the day will be between {} and {}".format(low, high);

righ_plan = RightPlan();
print(righ_plan.with_range(day_temp));