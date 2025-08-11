print('=====================================================================')
##############################################################################
############################## FILE HANDLING #################################
##############################################################################

# simple way
f = open('test-file.txt', 'r')

# modes - r, w, a (append), r+ (read-write), rb (read binary), wb (write binary)

#print(f.name)
#print(f.read())

f.close()

print('==================================')

# using context manager, preferred way, auto closing of file object for normal execution and when exceptions
with open('test-file.txt', 'r') as f:
    #print(f.read())         # ideal for small file size
    #print(f.read(100))      # read 100 characters at a time, once exhausted returns empty string

    # reading in chunks
    # size_to_read = 50
    # file_part_contents = f.read(size_to_read)
    # while len(file_part_contents) > 0:
    #     print(file_part_contents, end='')
    #     file_part_contents = f.read(size_to_read)


    #print(f.readlines())    # read all lines as list
    
    # for big files, efficient as lines read one by one
    #for line in f:
    #    print(line, end='')

    #print(f.readline(), end='')     # read one line at a time
    #print(f.readline(), end='')     # end - string appended after the last value, default a newline.

    file_part_contents = f.read(10)
    file_part_contents = f.read(10)
    print(f.tell())     # tells current position of our marker in the file
    f.seek(5)           # reset marker to 5th position again

# print(f.read())   # cant do it as its closed outside the block

print('==================================')

with open('test-file-2.txt', 'w') as f:
    f.write('This line is written from python file.\n')
    # print when used with file will also write to file instead of console output
    # it will also conveniently add a line space so that you dont have add one
    print('This line is written from python file.', file=f)

with open('test-file-2.txt', 'a') as f:
    f.write('This is second line appended from python file.')

with open('test-file.txt', 'r') as rf:
    with open('test-file-copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)