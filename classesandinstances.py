########################################################################
############################## CLASSES #################################
########################################################################

# Creating class but assigning variables everything externally
class User:
    pass

user1 = User()
user1.first = 'Guru'
user1.last = 'Todur'
user1.email = 'mail@company.com'
user1.pay = 50000

print(user1.first)

# Creating class and assigning variables internally in constructor
class Student:
    def __init__(self, first, last, major, aggregate):
        self.first = first
        self.last = last
        self.major = major
        self.aggregate = aggregate

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

student1 = Student('Guru', 'Todur', 'B.E.', 78)
print(student1.aggregate)

print(student1.fullname())
# when the above is called, its interpreted as below internally in Python
# that is why we write method definition as - def fullname(self) instead of def fullname()
# so both return same output
print(Student.fullname(student1))