class Add:
    def add(self, n1, n2):
        return n1+n2

class Multiply:
    def multiply(self, n1, n2):
        return n1*n2

class Calculator(Add, Multiply):
    def sub(self, n1, n2):
        return n1-n2

obj = Calculator()
print(obj.add(1,2))         # 3 is printed out
print(obj.multiply(3,2))    # 6 is printed out
