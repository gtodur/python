###############################################################################
############################## CLASS & STATIC METHODS #########################
###############################################################################

class Employee:
    hike = 1.06
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.num_of_emps += 1

    def hiked_pay(self):
        # cant access class variables directly
        # either access them via Class name or instance
        # because instances acquire class variables if not present in them
        return int(self.pay * Employee.hike)     # or self.hike
    
    @classmethod    #this decorator is to recognise it as class method not instance method
    def set_class_var_hike(cls, hike):  # takes in cls by default, as against self for instance method
        cls.hike = hike     # remember to set against class variable
    
    # using class method for creating an alternative constructor
    @classmethod
    def instance_from_str(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, int(pay))
    
    # it's worth having static method only if it doesn't make use of cls, self variables in its logic
    @staticmethod
    def is_workday(date):
        return not (date.weekday() == 5 or date.weekday() == 6)

emp1 = Employee('Guru', 'Todur', 10000)
emp2 = Employee('Test', 'Apprentice', 1000)
print(emp1.hiked_pay())
print(emp2.hiked_pay())

Employee.set_class_var_hike(1.10)   # emp1.set_class_var_hike(1.10) also works and changes class method value
print(emp1.hiked_pay()) # hike is reflected in emp1 instance
print(emp2.hiked_pay()) # hike is reflected here as well

print('====================================')

emp3_str = 'Harry-Brooks-35000'
emp4_str = 'John-Latham-55000'
emp5_str = 'Tim-White-65000'

emp3 = Employee.instance_from_str(emp3_str)
emp4 = Employee.instance_from_str(emp4_str)
emp5 = Employee.instance_from_str(emp5_str)

print(emp3.first, emp3.last, emp3.hiked_pay())
print(emp4.first, emp4.last, emp4.hiked_pay())
print(emp5.first, emp5.last, emp5.hiked_pay())


import datetime
date = datetime.date(2025, 7, 14)
print(Employee.is_workday(date))