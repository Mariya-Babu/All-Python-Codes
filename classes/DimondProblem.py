#Dimond Problem in Inheritance 
# X class
class X:
    def display(self):
        print('display method from X class')

# Y class
class Y:
    def display(self):
        print('display method from Y class')

# B class
class B(X):
    def display(self):
        print('display method from B class')
    pass

# C class 
class C(X):
    def display(self):
        print('display method from C class')
    pass

# D class
class D(B,C):
    # def display(self):
    #     print('display method from D class')
    pass

d = D()
d.display()
print(D.mro())




print('Hello')