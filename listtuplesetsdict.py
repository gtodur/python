print('=====================================================================')
######################################################################
############################## LISTS #################################
######################################################################

# can create empty list by assigning variable to [] or list()
empty_list = []
empty_list = list()

courses = ['IT', 'Electrical', 'Civil', 'Mechanical']

print(courses)
print(len(courses))
print(courses[0])   # first element of list
print(courses[-1])  # last element of list
print(courses[:2])
print(courses[1:])
print(courses[1:2])

print('==============================')

courses.append('E&E')
courses.insert(1, 'IS')
non_engg_courses = ['Arts', 'Politics']
courses.extend(non_engg_courses)
print(courses)

print('==============================')

courses.remove('IS')
popped_course = courses.pop()
print(popped_course)
print(courses)

print('==============================')

courses.reverse()
print(courses)

# in-place sort
courses.sort()
print(courses)

courses.sort(reverse=True)
print(courses)

# function which returns sorted list, also available min(), max(), sum()
sorted_courses = sorted(courses)
print(sorted_courses)

print('==============================')

print(courses.index('IT'))

print('Civil' in courses)   # returns true/false after finding item

print('==============================')

for course in courses:
    print(course)

# enumerate will return index and the actual value
for idx, course in enumerate(courses, start=1): # if index is to start from 1
    print(idx, course)

# join() is used to turn list values to string
courses_joined_str = ", ".join(courses)
print(courses_joined_str)
courses_joined_str = " - ".join(courses)
print(courses_joined_str)

# split() is used to turn string to list values which can be split
courses_split_list = courses_joined_str.split(' - ')
print(courses_split_list)

print('==============================')
print('==============================')
print('==============================')
#######################################################################
############################## TUPLES #################################
#######################################################################

# can create empty tuple by assigning variable to () or tuple()
empty_tuple = ()
empty_tuple = tuple()

# lists are mutable
list1 = ['bangalore', 'chennai', 'delhi', 'mumbai']
list2 = list1

print(id(list1))
print(id(list2))    # storage address same as list1

list1[0] = 'kolkata'    # since list1 and list2 point to same address, its changed in list2 too

print(list1)
print(list2)

# tuples are immutable but can be looped through and index access
tuple1 = ('bangalore', 'chennai', 'delhi', 'mumbai')
tuple2 = tuple1

print(id(tuple1))
print(id(tuple2))    # storage address same as tuple1

# tuple1[0] = 'kolkata'  -> cant do this in tuples as they are immutable  

print('==============================')
print('==============================')
print('==============================')
#####################################################################
############################## SETS #################################
#####################################################################

# can only create empty set by assigning variable to set()
empty_set = set()
# empty_set = {}    can't do this, it becomes a dictionary

# sets are unordered and prohibit duplicates
cars = {'Celerio', 'Alto', 'Swift', 'Brezza', 'Alto'}
print(cars)
print('Celerio' in cars)    # sets does this more efficiently than lists and tuples

export_cars = {'Celerio', 'Swift', 'Ignis', 'Baleno'}

# below operations are efficient in sets
print(cars.intersection(export_cars))
print(cars.difference(export_cars))
print(export_cars.difference(cars))
print(export_cars.union(cars))

print('==============================')
print('==============================')
print('==============================')
#############################################################################
############################## DICTIONARIES #################################
#############################################################################

# dictionaries contain keys and values in pairs
# can only create empty set by assigning variable to set()
empty_dict = {}

# keys can be strings or integers
user = {'name': 'guru', 'age': 25, 'courses': ['Math', 'CompSci'], 4: 'bangalore'}
print(user)
print(user['courses'])  # if key is absent, this way of retrieval gives out exception
print(user.get(4))
print(user.get(5))  # if key is absent, returns None
print(user.get('country', 'India'))     # if key found return its value, else return default value of India

user['phone'] = '08041190900'
user['name'] = 'Todur'

user.update({'age':35})     # acts like HTTP PATCH request, only update keys which are passed
print(user)

del user['age']
print(user)

user.update({'age': 45})
print(user)

poppedKeysValue = user.pop('courses') # remove key specified and returns value it held
print(poppedKeysValue)
print(user)

print(len(user))    # returns number of keys in dictionary
print(user.keys())
print(user.values())
print(user.items())

for key in user:
    print(key)  # only prints keys

for key, value in user.items():
    print(key, value)

print('==============================')
print('==============================')
print('==============================')
####################################################################################
############################## LIST COMPREHENSIONS #################################
####################################################################################

# for specific cases like return something for each items of a list
# for example, return square of a number for each number in the list

# for the above requirement, in case of pure list
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
newList = []
for num in nums:
    newList.append(num * num)
print(newList)

# through list comprehensions, its just simple
comprehension_list = [num * num for num in nums]
print(comprehension_list)

print("=====================================")

print("======== MAP + LAMBDA ============")
# using map + lambda in list comprehension
map_lambda_compre_list = map(lambda n: n*n, nums)
print(list(map_lambda_compre_list))

print("=====================================")

# I want n for each n in nums if n is even in list comprehension
compre_list = [n for n in nums if n%2 == 0]
print(compre_list)

print("=====================================")

print("======== FILTER + LAMBDA ============")
# using filter + lambda in list comprehension
filter_lambda_compre_list = filter(lambda n: n%2 == 0, nums)
print(list(filter_lambda_compre_list))

print("=====================================")

# I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'
# pure list way
new_list = []
for letter in 'abcd':
    for num in range(4):
        new_list.append((letter, num))
print(new_list)

# I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'
# list comprehension way
new_list = [(letter, num) for letter in 'abcd' for num in range(4)]
print(new_list)

print("=====================================")

print('==============================')
print('==============================')
print('==============================')
####################################################################################
############################## DICT COMPREHENSIONS #################################
####################################################################################

companies = ['Audi', 'BMW', 'Porsche', 'Mercedes', 'Volkswagen']
cars = ['R8', '320Li', 'Carrera', 'Maybach', 'Polo']
print(list(zip(companies, cars)))   # returns list of tuples -> [(company, car), (company, car) ...]

print("=====================================")

# I want a dict{company, car} for each company, car in zip(companies, cars)
# usual list way
new_dict = {}
for company, car in zip(companies, cars):
    new_dict[company] = car
print(new_dict)

# I want a dict{company, car} for each company, car in zip(companies, cars)
# dict comprehension way
new_dict = {company:car for company, car in zip(companies, cars) if company != 'Volkswagen'}
print(new_dict)

print('==============================')
print('==============================')
print('==============================')
####################################################################################
############################## SETS COMPREHENSIONS #################################
####################################################################################

# usual set way
nums = {1,2,3,3,5,4,6,7,9,8,6,5,9,2}
new_set = set()
for num in nums:
    new_set.add(num)
print(new_set)

# set comprehension way
new_set = {num for num in nums}
print(new_set)

print("=====================================")

# generator expressions
# similar to list comprehensions
# I want to yield n*n for each n in nums

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# generator way
def gen_func(nums):
    for n in nums:
        yield n*n

my_gen = gen_func(nums)

for n in my_gen:
    print(n)

print("=====")

# generator comprehension way
my_gen = (n*n for n in nums)

for n in my_gen:
    print(n)