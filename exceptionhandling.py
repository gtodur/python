print('=====================================================================')
###################################################################################
############################## EXCEPTION HANDLING #################################
###################################################################################

try:
    f = open('test-file.txt')
    #if f.name == 'test-file.txt':
    #    raise Exception
except FileNotFoundError as fnfe:
    print(fnfe)
except Exception as ex:
    print('Runtime exception occurred')
else:   # executed after successful execution of try block
    print('try block executed, now in else block')
    print(f.read())
    f.close()
finally:
    print('executing finally block')