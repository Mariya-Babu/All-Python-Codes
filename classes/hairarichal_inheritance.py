#Hairarichal_inheritance example practice
class Parent(object):

    def __init__(self,pname,page):
        self.pname = pname
        self.page = page
        print('Parent Constructor Called!')

    def work(self):
        print('Working at MicroSoft!')

    def parentDetails(self):
        print('Parent Details : ',end=" ")
        print(f'Name : {self.name}, age : {self.age}')


class Son(Parent):

    def __init__(self,name,age,pname,page):
        self.name = name
        self.age = age
        super().__init__(pname,page)
        print(f'Son Constructor Called!')

    def studing(self):
        print('Studing Computer Science')

    def sonDetails(self):
        super().parentDetails()
        print('Son Details : ',end=" ")
        print(f'Name : {self.name}, age : {self.age}')
    
    def Details(self):
        print(f'Name : {self.name}, age : {self.age}')

class Daughter(Parent):

    def studing(self):
        print('Studing Doctor!')
    
    


s = Son('Rishi',20,'Mark',40)
s.sonDetails()