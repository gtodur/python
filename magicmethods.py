######################################################################
############################## MAGIC METHODS #########################
######################################################################

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def emp_fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    # developer-friendly
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)
    
    # user-friendly
    def __str__(self):
        return '{} - {}'.format(self.emp_fullname(), self.pay)
    
    # Employee object __add__() implementation is to add two employees pay
    def __add__(self, another):
        return self.pay + another.pay
    
    # Employee object __len__() implementation is get length of employee fullname
    def __len__(self):
        return len(self.emp_fullname())
    
emp1 = Employee('Guru', 'Todur', 45000)
emp2 = Employee('Johnny', 'Smith', 40000)
# when __repr__() and __str__() both are present, __str__() gains precedence
print(emp1) # now internally calls __repr__() or __str__()
# but we can call individually whichever we want
print(emp1.__repr__())
print(emp1.__str__())

print('======================================')

# add dunder/magic method
print(1+2)
print('a'+'b')
# similar to below dunder method in python, so we can achieve polymorphism
print(int.__add__(1,2))
print(str.__add__('a','b'))

print('======================================')

print(emp1.__add__(emp2))

print('======================================')

# length dunder/magic method
print(len('Guru'))
# similar to below dunder method in python, so we can achieve polymorphism
print('Guru'.__len__())

print('======================================')

print(len(emp1))
