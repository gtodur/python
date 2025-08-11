print('=====================================================================')
#########################################################################
############################## ITERABLE & ITERATOR ######################
#########################################################################

# An object is an iterable if it contains the __iter__() upon dir(<object>)
# example - List

# An object is an iterator if it contains the __next__() upon dir(<object>)

nums = [1, 2, 3]
print(dir(nums))    # shows __iter__()
iter_nums = iter(nums)  # or equivalent of nums.__iter__(), converts list to an iterator now
print(iter_nums)
print(dir(iter_nums))   # shows __iter__() & __next__() that means its an iterable and iterator now.
print(next(iter_nums))  # 1st item in list
print(next(iter_nums))  # remembers 1 was printed, so this time returns 2
print(next(iter_nums))  # 3rd items from the list
# print(next(iter_nums)) - this will print StopIteration exception

print('============')

class MyRange:
    def __init__(self, start, end):
        self.value = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if(self.value >= self.end):
            raise StopIteration
        current = self.value
        self.value += 1
        return current
    
my_iter_nums = MyRange(1, 5)

# my_iter_nums is now an iterable
for num in my_iter_nums:
    print(num)

print('============')

# my_iter_nums is now an iterator too
# print(next(my_iter_nums))   # prints 1
# print(next(my_iter_nums))   # prints 2

# always remember if you iterate using iterable fully, then iterator tracks it as complete,
# so you get StopIteration for the first item itself

print('====================')

# Generator functions are also iterators even if they do not have __iter__() and __next__()
def my_range_gen(start, end):
    current = start
    while current < end:
        yield current
        current += 1

my_gen_iter_nums = my_range_gen(1,5)
# my_gen_iter_nums is now an iterable
# for num in my_gen_iter_nums:
#     print(num)

print('============')

# my_gen_iter_nums is now an iterator too
print(next(my_gen_iter_nums))   # prints 1
print(next(my_gen_iter_nums))   # prints 2