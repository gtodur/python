result = 'Hello'
print('Hello world from python')
print(type('Hello...'))

result = 5
print('Integer: ' + str(result))
print(type(result))

result = 5.0
print('Float: ' + str(result))
print(type(result))

result = None   # used when we don't have the value of the variable
print('NoneType: ' + str(result))
print(type(result))

result = True   # must be True/False exactly
print('Boolean: ' + str(result))
print(type(result))

print ('------------------')

print ('FUNCTIONS')

def greet(firstname, *lastname):
    lastname = '' if len(lastname) == 0 else lastname[0]
    print('Hello', firstname, lastname)

greet('Guru', 'Todur')
greet('Guruprasad')

print ('------------------')

print('DECORATOR FUNCTIONS')

def myLogger(func):
    def myWrapper():
        print('Before calling the function')
        func()
        print('After calling the function')
    return myWrapper

@myLogger
def printNumbers():
    for number in range(0, 100, 5):
        print(number)

printNumbers()
print ('------------------')

print('GENERATOR FUNCTIONS')

def getFirstTenSquaredNumbers():
    for num in range(1,11):
        yield num * num

numbersList = getFirstTenSquaredNumbers()   # numbersList here is an iterable

for num in numbersList:
    print(num)