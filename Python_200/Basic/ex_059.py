# Ex059 - Exception handling (5): try~except specific exception

import time
count = 1
try:
    while True:
        print(count)
        count += 1
        time.sleep(0.5)
except KeyboardInterrupt:   # Error when Ctrl+C is activated
    print('The program is terminated by user.')
