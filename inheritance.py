class Parent:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def display(self):
        print("Display method is called! from parent class ")
        print("Value of a is "+self.a)
        print("Value of  b is "+self.b)
        print("Value of c is "+self.c)
class Child(Parent):
    def __init__(self,d,e,f):
        self.d = d
        self.e = e
        self.f = f 
    def show(self):
        print("show method is called! from child class ")
        print("Value of a is "+self.a)
        print("Value of  b is "+self.b)
        print("Value of c is "+self.c)
        print("Value of e is "+self.e)
        print("Value of  fis "+self.f)
        print("Value of g is "+self.d)
child = Child()
print(child.d)
child.show()

