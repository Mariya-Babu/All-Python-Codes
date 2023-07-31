# positional arguments
def greet(msg, name):
    print(f'{msg} {name} How are you ? ')

greet('Hello','Mariya Babu')
greet('Rishi','Hi')

#keyword arguments
def keyword_args(msg,name,age):
    print(f'{msg} {name} How are you ?.\nyour age is = {age}')

keyword_args(msg='Hi',name='Mariya Babu',age=20)
keyword_args(name='Nani',age=18,msg='GoodMorning')
keyword_args('Hello','Rishi',age=5)
# keyword_args('Ola!',age=30,'Akash')  --> It will give error (positional arguments follows keyword arguments)
#Keyword arguments must follow positional arguments (positional_args, keyword_args)

def default_args(name,msg='Hi',age=20):
    #in parameters list default must be in last (positional_args, keyword_args)
    print(f'{msg} {name} How are you ?.\nyour age is = {age}')

default_args('Mariya Babu')
default_args('Rishi','Hello',5)
default_args('Nani','GoodMorning')


def args(*args):
    #   *parameter_name will accept list of parameters in tuple formate
    for i in args:
        print(f'{i}',end=" ")
args(1,2,3,4,5,6,7)
print('\a')

a , b = 10, 20
x , z = ('abc','cd')
def kyargs(**kyargs):
    # **kyargs will accept list of keyword argument in dictionary formate
    #  in parameters list *args will the first and **keyargs will be the last (*args,**keyargs)
    for value in kyargs:
        print(f'{value} {kyargs[value]}')
    
kyargs(msg='Hello',name='Mariya Babu',age=20)
kyargs(msg='Hi',name='Rishi',password=1234567,)