# Ex036 - Understanding list data structure ([])

list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
list3 = [1, 'a', 'abc', [1,2,3,4,5], ['a','b','c']]
list1[0] = 6        # [6,2,3,4,5] is printed out.
print(list1)
def myfunc():
    print('Hello')
list4 = [1, 2, myfunc]
list4[2]()          # 'Hello' is printed out.
