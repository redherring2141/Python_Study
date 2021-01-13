class MyClass:
    def __init__(self, txt):
        self.var = txt
        print('The value received as constructor argument is <' + self.var +'>.')

obj = MyClass('Cheolsoo')     # 'MyClass instance object is generated' is printed out
print(obj.var)      # 'Cheolsoo' is printed out
