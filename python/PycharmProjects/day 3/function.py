#function create
def welcome():
    print('welcome to mk')

welcome()   #funcion calling


#function with argument
#1
def great(name):
    print(f'hello {name},welcome')

great('mathan')   #funcion calling

#2
def minus(a,b):
    print(a-b)

minus(3,8)  #funcion calling

#return function
def plus(a,b):
    return a+b

result=plus(4,9)
print(result)

#*args function

def add(*args):
    total=0
    for num in args:
        total += num
    return total

print(add(1,2,7))

#kwargs function
def create_profile(**kwargs):
    print('user frofile')
    for key,value in kwargs.items():
        print(f'{key}:{value}')

create_profile(name='mkmathan',age='20',job='data engineer')