import sys

'''
Problem:
The use of a variable to describe a complex concept
like the role of a user in the system.
'''
class User(object):
    def __init__(self, role):
        self.role = role;
    
    def get_role(self):
        return self.role;

'''
Solution:
Build a class to represent the complex concept instead
of using a simple variable.
'''
class UserRole(object):
    def __init__(self, name, permissions):
        self.name = name;
        self.permissions = permissions;
    def validate_permissions(self):
        return "Valid permissions";
    def get_name(self):
        return self.name;
    def get_permissions(self):
        return self.permissions;

class RightUser(object):
    def __init__(self, role: UserRole):
        self.role = role;
    def get_role(self):
        return self.role.get_name();

try:
    input_role = sys.argv[1];
    input_permissions = sys.argv[2];
    role = UserRole(input_role, input_permissions);
    user = RightUser(role);
    print("User role is {}.".format(user.get_role()));
except Exception:
    print("Something went wrong!");