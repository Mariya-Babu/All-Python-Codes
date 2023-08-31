# This Programme is an example of Hybrid Inheritance

#University Class
class University:
    def __init__(self,uni_name):
        self.uni_name = uni_name
    
    def showDetails(self):
        print(f'Name of the university is : {self.uni_name}')
    

#Course Class
class Course(University):
    def __init__(self,uni_name,course_name):
        super().__init__(uni_name)
        self.course_name = course_name
    
    def showDetails(self):
        super().showDetails()
        print(f'Name of the course is : {self.course_name}')
    
#Branch Class 
class Branch(University):
    def __init__(self,uni_name,branch_name):
        super().__init__(uni_name)
        self.branch_name = branch_name
    
    def showDetails(self):
        super().showDetails()
        print(f'Name of the branch is : {self.branch_name}')


#Student Class
class Student(Course,Branch):
    def __init__(self,uni_name,course_name,branch_name,stu_name):
        # self.uni_name = uni_name
        # self.course_name = course_name
        # self.branch_name = branch_name
        # super(Course).__init__(uni_name,course_name)
        # super(Branch).__init__(uni_name,branch_name)
        # super().__init__(self,uni_name,course_name)
        # super().__init__(self,uni_name,branch_name)
        # super().__init__(uni_name,course_name)
        # Course.__init__(self,uni_name,course_name)
        Branch.__init__(self,uni_name,branch_name)
        self.stu_name = stu_name
    
    def showDetails(self):
        Course.showDetails()
        Branch.showDetails()
        print(f'Name of the student is : {self.stu_name}')

#Faculty Class
class Facutly(Branch):
    def __init__(self,uni_name,branch_name,fac_name):
        super().__init__(uni_name,branch_name)
        self.fac_name = fac_name

    def showDetails(self):
        super().showDetails()
        print(f'Name of the Facutly is : {self.fac_name}')


# u = University('RGUKT')
# print(u.uni_name)
# u.showDetails()

# c = Course('RGUKT','Python')
# print(c.course_name)
# print(c.uni_name)
# c.showDetails()

# b = Branch('RGUKT','CSE')
# print(b.uni_name)
# print(b.branch_name)
# b.showDetails()

s = Student('RGUKT','Python','CSE','Mariya Babu')

# print(s.uni_name)
# print(s.course_name)
print(s.branch_name)
print(s.stu_name)
s.showDetails()
