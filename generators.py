print('=====================================================================')
###############################################################
############################## GENERATOR ######################
###############################################################

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# list way
def squared_nums(nums):
    result = []
    for num in nums:
        result.append(num * num)
    return result

print(squared_nums(nums)) # prints the list that was returned with squared numbers

print('=======================')

# generator way
def squared_nums_generator(nums):
    for num in nums:
        yield num * num

nums_gen = squared_nums_generator(nums) # now nums_gen is an iterable and iterator too

# iterator
print(next(nums_gen))   # prints square of 1
print(next(nums_gen))   # prints square of 2

print('=======================')

# iterable
for num in nums_gen:
    print(num)  # prints the remaining numbers only (from 3*3=9), as it keeps track of last number

print('=======================')

# generator also has another feature similar to list comprehension
# list comprehension
list_compre_nums = [n*n for n in nums]
print(list_compre_nums)

# generator
gen_nums = (n*n for n in nums)
for num in gen_nums:    # once you have generator, use it via for loop for performance and time improvement
    print(num)

# the below also works, but it negates the performance and time improvement of generator, now its a normal list
# print(list(gen_nums))