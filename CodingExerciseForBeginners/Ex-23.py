#Convert given list of marks into grades {dictonary's practice problem}

#Grade Function takes marks and return grade
def grade(marks):
    if(marks<=100 and marks>=91):
        return 'A+'
    elif(marks<=90 and marks>=81):
        return 'A'
    elif(marks<=80 and marks>=71):
        return 'B+'
    elif(marks<=70 and marks>=61):
        return 'B'
    elif(marks<=60 and marks>=51):
        return 'C'
    elif(marks<=50 and marks>=41):
        return 'D'
    else:
        return 'F'

#Student_marks 
student_marks = {
    'Jenny' : 92,
    'Harry' : 78,
    'Dimpy' : 56,
    'Rahul' : 41,
    'Aniket' : 99,
    'Prem' : 34,
    'Address' : {
        'pin' : 4923983,
        'city' : 'abk'

    },
    'coursers' : ['py','java','c','c++']
}

list1 = [{},{},{}]
#student_grades
student_grades = dict()

for key, val in student_marks.items():
    g = grade(val)
    student_grades[key] = g

print(student_grades)

print(student_marks)