# Ex041 - Understanding local and global variables (global)

param = 10
strdata = 'global variable'

def func1():
    strdata = 'local variable'
    print(strdata)


def func2(param):
    param = 1


def func3():
    global param
    param = 50


func1()         #'local variable' is printed out
print(strdata)  #'global variable' is printed out
print(param)    # 10 is printed out

func2(param)
print(param)    # 10 is printed out

func3()
print(param)    # 50 is printed out



