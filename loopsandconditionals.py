print('=====================================================================')
#############################################################################
############################## CONDITIONALS #################################
#############################################################################

lang = 'python'
if lang == 'python':
    print('PYTHON')
elif lang == 'java':
    print('JAVA')
else:
    print('UNKNOWN')

name1 = 'Guru'
name2 = 'Guru'
print(id(name1))        # print obj location
print(id(name2))
print(name1 is name2)   # compare if both point to same obj location

# check if a number is between 1 and 20, python way
num = 21
print(1 <= num <= 20)

# All of th below evaluates to False
# False, None, Zero of any numeric type, empty seq('', (), []) or empty mapping({})

print('================================================================')
print('================================================================')
print('================================================================')

###################################################################################
############################## LOOPS & ITERATIONS #################################
###################################################################################

nums = [1,2,3,4,5]

for num in nums:
    print(num)

print('===============')

for num in nums:
    if num == 3:
        print('found' + f'{num}')
        break
    print(num)

print('===============')

for num in nums:
    if num == 3:
        print('found' + f'{num}')
        continue
    print(num)

print('===============')

for num in nums:
    for letter in 'Guru':
        print(letter, num)

print('===============')

for num in range(10):
    print(num)

print('===============')

for num in range(5, 10):
    print(num)

print('===============')

res = 1

while res < 100:
    print(res)
    res *= 2