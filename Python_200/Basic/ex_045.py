# Ex045 - Importing Python models (1): (import)

import time                     #Import Python's internal module 'time'
import ex_043_mylib             #Import 'mylib' module written
import ex_044_mypackage.mylib   #Import 'mylib' module in mypackage

time.sleep(1)                   #Stop for a second by using 'sleep' function
ret1=ex_043_mylib.add_txt('I\'m','Python.')  # Call 'add_txt' function inside 'ex_043_mylib' module
ret2=ex_044_mypackage.mylib.reverse(1,2,3)   # Call 'reverse' from 'mypackage.mylib' module

print(ret1)
print(ret2)
