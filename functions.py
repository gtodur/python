from functools import reduce

print('=====================================================================')
##########################################################################
############################## FUNCTIONS #################################
##########################################################################

def work_in_progress_func():
    pass    # something like <nothing here>

# writing pass within a function in progress returns None and not an error
print(work_in_progress_func())

def greeting_func(greet_type, name='Guest'):    # args with default values must be at last
    return f'{greet_type} {name}'

print(greeting_func('Hi', 'Guru'))

# passing value to param which has default value should be at last during method call
print(greeting_func('Hi', name='Guru'))

print('=====================================================================')
print('=====================================================================')
print('=====================================================================')
#################################################################################
############################## *ARGS & **KWARGS #################################
#################################################################################

def student_info(*args, **kwargs):
    """ This is a doc string explaining what the function is supposed to do."""
    print(args)
    print(kwargs)

student_info('Maths', 'Science', sport='Cricket', lang='Kannada')

courses = ['Maths', 'Science']
info = {'sport':'Cricket', 'lang':'Kannada'}

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

# both the parameters are interpreted as *args when passed as List and Dictionary
student_info(courses, info)

# specifying which part is *args and which is **kwargs
student_info(*courses, **info)

print('=====================================================================')
print('=====================================================================')
print('=====================================================================')
#################################################################################
############################## LAMBDA FUNCTIONS #################################
#################################################################################

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map() without lambda
def square(num):
    return num*num

# map(func, *iterables) --> returns map object
squared_nums = list(map(square, nums))
print(squared_nums)

# map() with lambda
squared_nums = list(map(lambda num: num*num, nums))
print(squared_nums)

print('===============')

# filter() without lambda
def check_even(num):
    return num%2 == 0

# filter(func, *iterables) --> returns map object
even_nums = list(filter(check_even, nums))
print(even_nums)

# filter() with lambda
even_nums = list(filter(lambda num: num%2 == 0, nums))
print(even_nums)

print('===============')

unsorted_list = [(1, 'b', 'hello'), (3, 'a', 'apple'), (2, 'c', 'world')]

# sorted() with lambda, sort by index value 2 then by index value 0
sorted_list = sorted(unsorted_list, key=lambda entry: entry[1] + entry[2])
print(sorted_list)

print('===============')

# reduce() with lambda, return sum of numbers without initializer
sum = reduce(lambda acc, num: acc + num, nums)
print(sum)

print('===============')

# reduce() with lambda, return max of numbers without initializer
max = reduce(lambda acc, num: acc if acc > num else num, nums)
print(max)

print('===============')