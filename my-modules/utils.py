print('Imported utils module')

pi = 3.14

def search(list, target):
    for idx, item in enumerate(list):
        if item == target:
            return idx
        
    return -1