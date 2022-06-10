'''
Problem:
A code uses an array to store data without
good label names
'''
row = [];
row.append("Manchister City");
row.append(34);

'''
Solution:
Build a class and use an object with proper
attribute names.
'''
class StdClass(object):
    pass

row = StdClass();
row.name = "Manchister City";
row.wins = 34;

print("The {} team won {} times".format(row.name, row.wins));