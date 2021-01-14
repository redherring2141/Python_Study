# Ex040 - Understanding function arguments

def add_txt(t1, t2='Python'):
    print(t1+':'+t2)

add_txt('Best')                 # 'Best:Python' is printed out.
add_txt(t2='Korea', t1='1st')   # '1st:Korea' is printed out.

def func1(*args):
    print(args)

def func2(width, height, **kwargs):
    print(kwargs)

func1()             # Empty tuple () is printed out.
func1(3, 5, 1, 5)   # (3, 5, 1, 5) is printed.
func2(10, 20)       # Empty dictionary {} is printed out.
func2(10, 20, depth=50, color='blue')   # {'depth':50, 'color':'blue'} is printed out.
