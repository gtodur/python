import os

f = open('test-file.txt', 'r+')
print(f.read(20))
f.close()

os.mkdir('new')

with open('new/new-file.txt', 'w') as f:
    f.write('This is a new file')

with open('new/new-file.txt', 'r') as f:
    print(f.read())

if os.path.exists('new/new-file.txt'):
    print('path and file exists')
else:
    print('path and file DOES NOT exists')    

os.remove('new/new-file.txt')
os.rmdir('new')

print('path and file exists') if os.path.exists('new/new-file.txt') else print('path and file DOES NOT exists') 