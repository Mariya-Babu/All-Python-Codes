class Instructor:
    def __init__(self,name,address,s='HelloWorld!',flws=0):
        print('Object created to this Class Instructor.')
        self.name = name
        self.address = address
        self.followers = flws
        self.self = s


instructor_1 = Instructor('Mariya','Addanki')
instructor_2 = Instructor('Babu','Mylavaram',100)

print(instructor_1)
print(instructor_2)
print('Instructor_1')
print(instructor_1.name)
print(instructor_1.address)
print(instructor_1.followers)

print('\n\nInstructor_2')
print(instructor_2.name)
print(instructor_2.address)
print(instructor_2.followers)


print(instructor_1.self)


class Abc:
    def __init__(self,Abc,Abc,__init__):
        self.Abc = Abc
        self.__init__ = __init__

a = Abc('Hello','Hi','World')

print(a.Abc)
print(a.__init__)