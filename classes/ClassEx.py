class Emp:
    id = 0
    name = 'Mariya Babu'
    def display(self):
        print(self.id,self.name)


emp1 = Emp()
emp1.display()


class Std:
    def __init__(self,name,id,age):
        self.name = name
        self.id = id
        self.age = age

    def display(self):
        print(self.name)
        print(self.id)
        print(self.age)

std1 = Std('Rishi',101,20)
std1.display()
print(std1.age)
print(std1.name)
print(std1.id)

print(getattr(std1,'name'))
print(hasattr(std1,'id'))
print(delattr(std1,'age'))
print(setattr(std1,'collage','IIIT-Nuzvid'))
print(getattr(std1,'collage'))

print(std1__doc__)
print(std1__dict__)
print(std1__module__)