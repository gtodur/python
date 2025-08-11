name = 'Guruprasad Todur'
########################################################################
############################## STRINGS #################################
########################################################################

print(len(name))
print(name[11])
print(name[4:10])
print(name[:4])     # from starting
print(name[11:])    # to end
print(name.count('a'))
print(name.find('pra'))     # returns index if found else -1

full_name = name.replace(' ', ' Umesh ')
print(full_name)

salutation = 'Hello'
print('{}, {}. Welcome to Python!'.format(salutation, full_name))
print(f'{salutation}, {full_name.upper()}. Welcome to Python!')

# list methods and attributes
#print(dir(full_name))       # of a variable
#print(help(str.find))      # of a object or its method

print('================================================================')
print('================================================================')
print('================================================================')

########################################################################
######################## INTEGERS & FLOATS #############################
########################################################################

print(5 / 3)    # returns 1.6666666666666667
print(13 // 2)   # floor division, returns 6
print(round(3.5))   # rounds to nearest even, returns 4
print(round(2.5))   # rounds to nearest even, returns 2
print(round(13.155, 2))

amount1 = '100'
amount2 = 200
print((amount1) + amount2)   # cast to int