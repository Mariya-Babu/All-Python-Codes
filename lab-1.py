import random
#Guessing of Number
#Display Hello World!
print("Hello World!")
# Greatest of 3 numbers 
a = 4
b = 9
c = 3
if(a>b):
    if(a>c):
        print("A is greatest")
    else:
        print("C is greatest")
else:
    if(b>c):
        print("B is greatest")
    else:
        print("C is greatest")
#Simple Calculator
str = '''''
+ Addition 
- Subtraction
* multiplication
/ division
'''
while(1):
    a = int(input("Enter first num for calc : "))
    b = int(input("Enter second num for calc : "))
    print(str)
    opt = input("Enter your option : ")
    if(opt=='+'):
        print(f"Addition of {a} and {b} numbers is : ",a+b)
    elif(opt=='-'):
        print(f"Subtraction of {a} and {b} numbers is : ",a-b)
    elif(opt=='*'):
        print(f"Multiplication of {a} and {b} numbers is : ",a*b)
    elif(opt=='/'):
        print(f"Division of {a} and {b} numbers is : ",a/b)
    else:
        print("Invalid Option.....")
    exit = int(input("If you want to exit press 0"))
    if(exit==0):
        break




#create a string using double quotes
string1 = "Python programming"
#create a string using quotes
string1 = 'Python programming'
#create string type variables
name = 'Python'
print(name)
message = "I love python"
print(message)
greet = 'hello'
#access 1st index element
print(greet[1]) # "e"
greet = 'Hello'
#access character from 1st index to 3rd index
print(greet[1:4]) #'ell
message = 'Hola Amigos'
message[0] = 'H' #will give you error
print(message)
#assign new string to message variable
message = 'Hello Friends'
print(message) #it will print 'Hello Friends'

#multiline string
message = """
Never gonna give you up
Never gona let you down
""" 
print(message) 
#Never gonna give you up
# Never gona let you down
str1 = 'Hell, world'
str2 = 'I love Python'
str3 = 'Hello, world!'
#compare str1 and str2
print(str1 == str2) #False
#compare str1 and str3
print(str1 == str3) #True
greet = "Hello"
name = 'Jack'
#Using  + Operator
result = greet + name
print(result) # Hello, Jack
#count length of great string
print(len(greet)) #5
print('a' in 'programme') # true
print('at' not in 'battle') # Fale
# example = "He said, "What's There?""
# print(example) #throws error
#escape double quotes
example = "He said, \"What's there?\""
#escape single quotes
example = 'He said, "What\'s there?" ' #He said, "What's there?"
name = 'Cathy'
country = 'UK'
print(f'{name} is from {country}') #Cathy is from UK
#A list with 3 integers
numbers = [1, 2, 5]
print(numbers) #[1, 2, 5]
#empty list
my_list = []
#list with mixed data types
my_list = [1, "Hello", 3.4]
languages  = ["Python", "Swift", "C++"]
#access item at index 0
print(languages[0]) #Python
#access item at index 2 
print(languages[2]) #C++
#access item at index 0 (negative indexing)
print(languages[-1]) # c++
#access item at index 2 (negative indexing)
print(languages[-3]) #Python
#List slicing in python
my_list = ['P','r','p','g','r','a','m','i','z']
#items from index 2 to index 4
print(my_list[2:5]) #['p','g','r']
#items from index 5 to end
print(my_list[5:]) #['a','m','i','z']
#items beginning to end
print(my_list[:]) #['P','r','p','g','r','a','m','i','z']
numbers = [21, 34, 54, 12]
print("Before Append:",numbers) #[21, 34, 54, 12]
#using append method
numbers.append(32) 
print("After Append:",numbers) #[21, 34, 54, 12, 32]
numbers.append(32)
prime_numbers = [2, 3, 5] 
print("List:", prime_numbers) #[2, 3, 5] 
even_numbers = [4, 6, 8]
print("List2:", even_numbers) #[4, 6, 8]
#join two lists
prime_numbers.extend(even_numbers)
print("List after append:", prime_numbers) #[2, 3, 5, 4, 6, 8] 
languages = ['Python', 'Swift', 'C++']
#Changing the third item to 'c'
languages[2] = 'C'
print(languages) #languages = ['Python', 'Swift', 'C']
languages = ['Python', 'Swift', 'C++', 'Java', "Rust", 'R']
#deleting the second item
del languages[1]
print(languages) #['Python','C++', 'Java', "Rust", 'R']
#deleting the last item
del languages[-1]
print(languages) #['Python','C++', 'Java', "Rust"]
#deleting the first item
del languages[0]
print(languages) #['C++', 'Java', "Rust"]
languages = ['Python', 'Swift', 'C++', 'Java', "Rust", 'R']
#remove 'Python' from the list
languages.remove('Python')
print(languages) #['Swift', 'C++', 'Java', "Rust", 'R']
languages = ['Python', 'Swift', 'C++']
#iterating through the list
for language in languages:
    print(language)
#'Python'
#'Swift'
#'C++'
print('C' in languages) #False
print('Python' in languages) # True
languages = ['Python', 'Swift', 'C++']
print("List: ",languages)
print("Total Elements: ",len(languages)) # 3
numbers = [number*number for number in range(1,6)]
print(numbers) # [1, 4, 9, 16, 25]
numbers = [x*x for x in range(1, 6)]
# is equivalent to 
numbers = []
for x in range(1,6):
    numbers.append(x*x)
print(numbers) # [1, 4, 9, 16, 25]  
#Different types of tuples 
#Empty tuple
my_tuple = ()
print(my_tuple) #()
#Tuple having integers
ny_tuple = (1, 2, 3)
print(my_tuple) #(1, 2, 3)
#tuple with mixed data types
my_tuple = (1, "Hello", 3.4)
print(my_tuple) #(1, "Hello", 3.4)
#nested tuple
my_tuple = ("mouse", [8 , 4, 6], (1, 2, 3))
print(my_tuple)  #("mouse", [8 , 4, 6], (1, 2, 3))
my_tuple = 1, 2, 3
my_tuple = 1, "Hello", 3.4
var1 = ("Hello") #string
var2 = ("Hello",) #tuple
var1 = ("hello")
print(type(var1))#<class 'str'>

#creating a tuple having one element
var2 = ("hello",)
print(type(var2)) #<class 'tuple'>
#Parentheses is optional
var3 = "hello",
print(type(var3)) #<class 'tuple'>

#accessing tuple elements using indexing
letters = ("p","r","o","g","r","a","m","i","z")
print(letters[0]) #prints "p"
print(letters[5]) #prints "a"

#accessing tuple elements using negative indexing
letters = ("p","r","o","g","r","a","m","i","z")
print(letters[-1]) #prints 'z'
print(letters[-3]) #prints 'm'

#accessing tuple elements using slicing 
my_tuple = ("p","r","o","g","r","a","m","i","z")
#elements 2nd to 4th index
#elements beginning to 2nd
print(my_tuple[2:4]) #prints("r","o","g")
#elements beginning to 2nd 
print(my_tuple[:-7]) #prints ("p","r")
#elements 8th to end
print(my_tuple[7:]) #prints ("i","z")
#elements begiing to end
print(my_tuple[:]) #prints ("p","r","o","g","r","a","m","i","z")
my_tuple = ('a','p','p','l','e')
print(my_tuple.count('p')) #prints 2
print(my_tuple.index('l')) #prints 3
languages = ('Python','Swift','C++')
#iterating through the tuple
for language in languages:
    print(language) 
#Python
#Swift
#C++
languages = ('Python','Swift',"C++")
print('C' in languages) # False
print('Python' in languages) #True


# SETS 
#create a set of integer type
student_id = {112, 114, 116, 118, 115}
print('student_ID : ',student_id)

#create a set of string type
vowel_letters = {'a','e','i','o','u'}
print('vowel Letters: ',vowel_letters)  # vowel Letters: {'a','e','i','o','u'}
#create a set of mixed data types
mixed_set = {'Hello', 101, -2, 'Bye'}
print('Set of mixed data types: ',mixed_set) # Set of mixed data types:  {'Hello', 101, -2, 'Bye'}

#create an empty set 
empty_set = set()
#create an empt dictionary
empty_dictionary = {}
#check data type of empty_set
print('Data type of empty_set: ',type(empty_set))

#check data type of empty_dictionary_set
print('Data type of empty_dicitonary_set: ',type(empty_dictionary))
numbers = {2, 4, 6, 2, 8}
print(numbers) #prints {2, 4, 8, 6}
numbers = {21, 34, 54, 12}
print('Initial Set : ',numbers)
#using add() method
numbers.add('32')
print('Updated Set:',numbers) #Updated Set: {32, 34, 12, 54}
companies = {'Lacoste', 'Ralph Lauren'}
tech_companies = ['apple','google','apple']
companies.update(tech_companies)
print(companies) #Output : {'google', 'apple', 'Lacoste', 'Ralph Lauren'}
languages = {'Swift', 'Java', 'Python'}
print('Initial Set: ',languages)  #Initial Set: {'Swift', 'Java', 'Python'}
#remove 'Java' from a set
removedValue = languages.discard('Java')
print('Set after remove(): ',languages) #Set after remove {'Swift','Python'}
fruits = {"Apple","Peach","Mango"}
#for loop to access each fruits
for fruit in fruits:
    print(fruit)
#Mango
#Peach
#Apple
even_numbers = {2, 4, 6, 8}
print('Set: ',even_numbers) #Set: {8, 2, 4, 6}
#find number of elements
print('Total Elements: ',len(even_numbers)) #'Total Elements: '4

#first set
A = {1, 3, 5}
#second set
B = {0, 2, 4}
#perform union operation using |
print('Union using|: ',A|B) #Union using|: {0, 1, 2, 3, 4, 5}
#perform union operation using union()
print('Union using union(): ',A.union(B)) #Union using union(): {1, 3, 5,0, 2, 4}

#first set
A = {1, 3, 5}
#second set
B = {1, 2, 3}
#perform intersection operation using & 
print('Intersection operation using &: ',A & B) #Intersection operation using &: {1,3}
#perform intersection operation using intersection()
print('Intersection using intersection(): ',A.intersection(B)) #Intersection operation using intersection(): {1, 3}

#first set
A = {2, 3, 5}
#second set
B = {1, 2, 6}
#perform difference operation using &
print('Difference operation using -:', A - B) #Difference operation using -: {3, 5}
#perform difference operation using difference()
print('Difference using difference(): ',A.difference(B)) #Difference operation using difference(): {3, 5}

#first set
A = {2, 3, 5}
#second set
B = {1, 2, 6}
#perform symmetric operation using ^
print('Symmetric Difference operation using ^:', A ^ B) # Symmetric Difference operation using ^: {1, 3, 5, 6}
#perform difference operation using difference()
print('Difference using difference(): ',A.symmetric_difference(B)) # Symmetric Difference operation using symmetri_difference(): {1, 3, 5, 6}

#first set 
A = {1, 3, 5}
#second set
B = {3, 5, 1}
#perform equality between to sets using ==
if A==B:
    print('Set A and Set B are equal')
else:
    print('Set A and Set B are not equal')
#Set A and Set B are  not equal

# Dictionary 
capital_city = {"Nepal":"Kathmandu","Italy":"Rome","England":"London"}
print(capital_city) #prints {"Nepal":"Kathmandu","Italy":"Rome","England":"London"}
#dictionary with keys and values of different data types
numbers = {1:"One", 2:"Two", 3:"Three"}
print(numbers) #{1:"One", 2:"Two", 3:"Three"}
capital_city = {"Nepal":"Kathmandu","England":"London"}
print('Initial Dictionary: ',capital_city) #Initial Dicitonary: {"Nepal":"Kathmandu","England":"London"}
capital_city["Japan"] = "Tokyo"
print("Updated Dictionary: ",capital_city) #Updated Dictionary: {"Nepal":"Kathmandu","England":"London","Japan":"Tokyo"}

student_id = {111:"Eric", 112:"Kyle",113:"Butters"}
print('Initial Dictionary: ',student_id) #Initial Dicitonary: {111:"Eric",112:"Kyle",113:"Butters"}
student_id[112] = 'Stan'
print('Updated Dicitonary: ',student_id) #Updated Dictionary: {111:"Eric",112:"Stan",113:"Butters"}
student_id  = {111:"Eric",112:"Kyle",113:"Butters"}
print(student_id[111]) #prints Eric
print(student_id[113]) #prints Butters

student_id = {111:"Eric",112:"Kyle",113:"Butters"}

#print(student_id[211]) #Output: KeyError: 211
student_id = {111:"Eric",112:"Kyle",113:"Butters"}
#delete student_id ditionary
del student_id
# print(student_id)
#Output: NameError: name 'student_id' is not defined

# Memerbership Test for Dictionary Keys 
squares = {1:1, 3:9, 5:25, 7:49, 9:81}
print(1 in squares) #prints True
print(2 not in squares) #prints True
#memebership tests for keys only not value
print(49 in squares) #prints True

# Iterating throught a Dicitonary 
squares = {1:1, 3:9, 5:25, 7:49, 9:81}
for i in squares:
    print(squares[i]) 
#1
#9
#25
#49
#81