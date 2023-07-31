#Nested Dictonary Practice

def add_new_student(name,roll_no,age,course):
    d = {
        'Name' : name,
        'roll_no' :  roll_no,
        'age' : age,
        'cousrse' : course
    }
    return d


student_data = [
    {
        'Name' : 'Ram',
        'roll_no' : 10,
        'age' : 20,
        'course' : 'Python'
    },
    {
        'Name' : 'Mohan',
        'roll_no' : 20,
        'age' : 22,
        'course' : 'Java'
    }
]

student_data.append(add_new_student('Shyam',22,18,'C++'))

print(student_data)

def fun_name(parameters):
    #code
    return 





