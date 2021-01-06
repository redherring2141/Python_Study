from time import sleep
from ex_044_mypackage import mylib
from ex_044_mypackage.mylib import reverse

sleep(1)                        # Call sleep function from time module
mylib.add_txt('I\'m', 'Python') # Call add_txt function from mypackage.mylib module
reverse(1,2,3)                  # Call reverse function from mypackage.mylib module
