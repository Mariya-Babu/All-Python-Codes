#Multilevel Inheritance Practice
class GrandParent(object):
    hello = 'Hello'
    def __init__(self):
        print('Grand Parent Constructor Called!')

    def assets(self):
        print('30 Acers of Land')
    
    def work(self):
        print('Work in the field!')

class Parent(GrandParent):

    def __init__(self,age):
        super().__init__()
        self.age = age
        print('Parent Constructor is Called!')
    def job(self):
        print('Computer Scientist')
    
    def work(self,a):
        print('Work in MicroSoft')
        print(f'a = {a}')

    def work(self,a,b):
        super().__init__()
        print('Left MicroSoft and Working at Apple')
        print(f'a = {a} b = {b} ')

class Child(Parent):

    def __init__(self,age):
        super().__init__(age)
        # self.age = age
        print('Child Constructor is called!')

    def studing(self):
        print('Studing Btech Computer Science')

    def work(self):
        print('Trying to get job in the google!')
        # print(f'a = {a}')
        print(Parent.hello)

    def pwork(self):
        super().work()



class GrandChild(Child):

    def __init__(self,name,age):
        super().__init__(age)
        self.name = name
        print('GrandChild Constructor is called!')

    # def age(self):
    #     print('I am having 10 years!')

    def hello(self):
        print('Hello World!')

    def work(self):
        super().work()
        print('I am not a  working professional!')

    def age(self):
        print('My age is 10 years! ')

gc = GrandChild('Mariya Babu',20)
gc.work()
# gc.age()
gc.hello()
gc.age()


