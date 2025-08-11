#################################################################
############################## SUBCLASS #########################
#################################################################

class Employee:
    hike = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def hiked_pay(self):
        # cant access class variables directly
        # either access them via Class name or instance
        # because instances acquire class variables if not present in them
        return int(self.pay * self.hike)     # Employee.hike or self.hike
    
    def emp_fullname(self):
        return '{} {}'.format(self.first, self.last)
    
class Developer(Employee):
    hike = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang
    
emp = Employee('Guru', 'Todur', 10000)
emp_dev = Developer('Test', 'Apprentice', 10000, 'Java')
print(emp.hiked_pay())
print(emp_dev.hiked_pay())
print(emp_dev.prog_lang)

print('===================================================')

class Manager(Employee):
    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees == None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employees(self):
        for emp in self.employees:
            print('-->', emp.emp_fullname())

manager = Manager('James', 'Bond', 90000, [emp])
print(manager.emp_fullname())
manager.print_employees()
manager.add_emp(emp_dev)
manager.remove_emp(emp)
manager.print_employees()

# isinstance()
print(isinstance(manager, Manager))    # True
print(isinstance(manager, Employee))   # True
print(isinstance(emp_dev, Manager))    # False

# issubclass()
print(issubclass(Manager, Employee))    # True
print(issubclass(Manager, Developer))   # False