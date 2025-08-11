########################################################################
############################## CLASS VARIABLES #########################
########################################################################

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
        return int(self.pay * self.hike)     # or self.hike

emp1 = Employee('Guru', 'Todur', 10000)
emp2 = Employee('Test', 'Apprentice', 1000)
print(emp1.hiked_pay())
print(emp2.hiked_pay())

print(Employee.__dict__)    # displays 'hike': 1.06 too
print(emp1.__dict__)    # displays {'first': 'Guru', 'last': 'Todur', 'pay': 10000}, no 'hike': 1.06

Employee.hike = 1.08
print(emp1.hiked_pay()) # hike is reflected in emp1 too as its copied to all instances
print(emp2.hiked_pay()) # hike is reflected here as well

emp1.hike = 1.10
print(emp1.hiked_pay()) # only emp1 copy is changed to 1.10
print(emp2.hiked_pay()) # emp2 hike is still 1.08
# bear in mind it depends on what is used inside hiked_pay()
# if its Employee.hike both are 1.08
# else if its self.hike then only emp1 copy is updated to 1.10, emp2 remains at 1.08
# also using self.hike allows sub-classes to change the hike amount for them

print(Employee.num_of_emps)