# To import a user created module from local system - 
    # append the directory in sys.path
    # add the directory in environment variables under key PYTHONPATH
import sys
# add the module path location to the system path variable
#sys.path.append('D:\GURU\GitHub\python-workspace\learn-python\my-modules')

#import utils
#import utils as u
from utils import search, pi
import os

########################################################################
############################## MODULES #################################
########################################################################
nums = [23, 45, 53, 51, 60, 31, 59, 86, 59, 20]
print(search(nums, 80))

print('pi value is', pi)
print(sys.path)     # all the locations from where the modules are loaded
print(os.getenv('PYTHONPATH'))

print('===============================================================')
########################################################################
############################## PACKAGES ################################
########################################################################

# pip help
# pip search <name>
# pip install <name>
# pip list
# pip uninstall <name>
# pip list --outdated
# pip install -U <name>     update package to latest version
# pip freeze > requirements.txt     get list of all packages installed into a file
# pip install -r requirements.txt

# update all packages at once
# pip freeze --local | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip install -U