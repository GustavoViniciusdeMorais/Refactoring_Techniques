import sys

'''
Problem:
You have a method that receives parameters from the same
type or origin.
'''
def amount_received_in(date_start, date_end):
    return "Ammount received between {} and {}".format(date_start, date_end);

'''
Solution:
Build an object to represent the parameters from the same
type or origin.
'''
class AmmountDate(object):
    def __init__(self, date_start, date_end):
        self.date_start = date_start;
        self.date_end = date_end;
    
    def get_date_start(self):
        return self.date_start;
    
    def get_date_end(self):
        return self.date_end;

def right_ammount_received_in(ammount_date):
    return "Ammount received between {} and {}".format(ammount_date.get_date_start(), 
        ammount_date.get_date_end());

try:
    date_start = sys.argv[1];
    date_end = sys.argv[2];
    ammount_date = AmmountDate(date_start, date_end);
    result = right_ammount_received_in(ammount_date);
    print(result);
except Exception as e:
    print(e);