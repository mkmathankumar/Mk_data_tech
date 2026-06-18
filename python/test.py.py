# #task1
# print("python\nis\npopular\nhigh-level\nprogramming\nlanguage")

# #task2
# print('python\ncan\nbe\nused\non\na\nserver\nto\ncreate\nwebapplication')

# #task3
# a=15
# b=7
# c=a%b
# print(c) 


# #task 4
# word="progr  amming"
# result="".join(word.split())
# print(result)

# #task 5
# num='extension'
# print(num.replace('s','c'))

# #task 6
# B='Baby'
# print(B.replace('B','Z'))

# #task 7
# a=10
# b=20
# count=a+b
# print('sum is',count)

# #task 8
# first_name='mk'
# last_name='math'
# full_name=first_name+last_name
# print(full_name)

# #task 9
# name='mathan'
# age=int(21)
# height=float(167.5)
# is_18_or_above=age>= 18

# print(name)
# print(age)
# print(height)
# print(is_18_or_above)

# #day 7
# #task1
# a=['joe','jhon','jimmy','jim']
# a.insert(2,'tommy')
# print(a)

# #task2
# b=['joe','jhon','jimmy','jim']
# b[3]='harry'
# print(b)

# #task3
# c=[1,2,3]
# d=['arun','karthi','kavya']
# print(f"{c[0],d[0],c[1],d[1],c[2],d[2]}")


# #task4
# z=['banana','cherry','watermelon']
# z[0]='grapes'
# z[2]='orange'
# print(z)


# #day 8
# #task 1

# a=['welcome','to','india','2026']
# for i in a:
#     print(i)

# b=['welcome','to','india','2026']
# i=0
# while i<len(b):
#     print(b[i])
#     i+=1

# #task 2
# num=[1,2,3,4,5]
# num.reverse()
# print(num)

# #task 3
# sum=[100,800,500,200,400,300]
# sum.sort(reverse=True)
# print(sum)

# #task 4
# B=[1000,20000,5000,20000]
# B=list(set(B))
# B.sort()
# print(B)

# #task 5
# c=[1,2,3]
# d=['arun','karthi','kavya']
# e=c+d
# print(e)
# f=list(zip(c,d))
# print(f)


# #task 6
# c=[1,2,3]
# d=['arun','karthi','kavya']
# g=[]
# for i,j in zip(c,d):
#     g.append((i,j))
#     print(g)
# print(g)

# #day 9 tupple methods
# #task 1
# # to get the value
# a=('john','kayal','deepak')
# print(a[1])

# #task 2 
# # if method 

# if 'deepak' in a:
#     print('yes')
# else:
#     print('no')

# # task 3 
# # to replace the tupple
# a=('john','kayal','deepak')
# b=list(a)
# b[1]='janani'
# a=tuple(b)
# print(a)

# #task 4
# a=('john','kayal','deepak','rohith')
# print(a)
# (white,grreen,blue,red)=a
# print(blue)
# print(white)

# #task 5
# a=('john','kayal','deepak','rohith','kiran','janani')
# print(a)
# (white,grreen,*red)=a
# print(red)
# print(white)

# # two tupple join method
# a=(1,2,3)
# b=('y','z','x')
# c=a+b
# print(c)
# # to convert the tupple to list then use all list methods in the tupple




# #dictionary
# #pop()
# x={'name':'kavya',
#    'age':20
#    }

# print(x)
# y=x.pop('age')
# print(y)
# print(x)

# z={'name':'kavya',
#    'age':20
#    }
# print(z)
# w=z.popitem()
# print(w)
# print(z)

# #clear

# a={'name':'kavya',
#    'age':20
#    }
# a.clear()
# print(a)

# #get
# a={'name':'kavya',
#    'age':20
#    }
# b=a.get('age')
# print(b)
# #or
# b=a['age']
# print(b)
# # to get valuues,keys and items
# b=a.keys()
# print(b)
# b=a.values()
# print(b)
# b=a.items()
# print(b)

# #add/update
# #single value update
# a['city']='chennai'
# print(a)
# #multiple value update
# a.update({'marks':95,'grade':'A'})
# print(a)
# #to replace the dict value
# a['age']=20
# print(a)

# #day12
# #task 

# x={'name':'juli',
#    'age':25,
#    'colour':'black',
#    'course':'python',
#    'number':6
#    }
# #1

# y=x.get('colour')
# print(y)

# #2

# x['course']='java'
# print(x)

# #3
# x['time']=x.pop('age')
# x['time']=10
# print(x)
# #4

# x={'name':'juli',
#    'age':25,
#    'colour':'black',
#    'course':'python',
#    'number':6
#    }

# x.popitem()
# print(x)

# #5

# x={'name':'juli',
#    'age':25,
#    'colour':'black',
#    'course':'python',
#    'number':6
#    }
# y=x.keys()
# print(y)
# y=x.values()
# print(y)

# #dict.keys

# a=('a','b','c')
# b=(1,2,3)
# x=dict.fromkeys(a,b)
# print(x)

# #zip methd
# a=('a','b','c')
# b=(1,2,3)
# x=dict(zip(a,b))
# print(x)

# #setdefault

# a={'a':1,'b':2}
# a.setdefault('c',3)
# print(a)


# a={'a':1,'b':2}
# a.pop('b')
# a.setdefault('b',3)
# print(a)

# student={'name':'juli',
#    'age':25,
#    'colour':'black',
#    'course':'python',
#    'number':6
#    }
# print('name' in student)
# print('marks' not in student)
# print('name' is student)

# #if methods
# #tasks
# a=[1,2,3,4,5,6,7,8,9,10]
# if len(a) >= 2:
#     print('sec last value',a[3])
#     old=a[2]
#     a[2]=10
#     print("old value:",old)
#     print('new value:',a[2])

# else:
#     print('list must hahe atleast two value')


# def voting(age):
#     if age >=18:
#         print('eligible to vote')
#     else:
#         print('not eligible')

# voting(20)
# voting(15)


# #for loop
# #tasks
# '''
# a=int(input('enter number:'))
# b=int(input('enter number:'))

# for i in range(1):
#     print(a+b)
#     print(a-b)
#     print(a*b)
#     print(a/b)
#     print(a%b)
#     print(a**b)
#     print(a//b)

# '''
# '''
# user='admin'
# password='1234'

# for i in range(3):
#     u = input('enter user name')
#     p = input('enter password')

#     if u == user and p==password:
#         print('login successfully')
#         break
#     else:
#         print('wrong user name password')

# else:
#     print('too many attempts')

# '''

# #while loop& for loop
# #tasks
# a={'name':'harish',
#    'age':25,
#    'course':'python'
#    }

# for i in a:
#     print(i,':',a[i])


# b=['hello','john','how','are','you']
# print('using for loop')
# for i in b:
#     print(i)

# print('using while loop')
# i=0
# while i<len(b):
#     print(b[i])
#     i+=1


# s='programming'
# print('using for loop')
# for i in s:
#     print(i)
    
# print('using while loop')
# i=0
# while i<len(s):
#     print(s[i])
#     i+=1


# print('1to20')
# for i in range (1,21):
#     print(i)

# print('reverse')
# for i in range (20,0,-1):
#     print(i)

# print('1to20')
# i=1
# while i<=20:
#     print(i)
#     i+=1

# print('reverse')
# i=20
# while i>=1:
#     print(i)
#     i-=1

# #functions
# #basic syntax

# def function_name():
#     print("Hello")


# #oops - object oriented programming language
# #basic sntax for class 
# class car:
#     pass
# car1=car()
# car2=car()

# print(type(car1))

# #use _init_
# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

# s1=student('alice',22)
# s2=student('bob',25)

# print(s1.name,s1.age)
# print(s2.name,s2.age)

# #inheritance

# #parent class
# class Person:

#     def __init__(self, name):
#         self.name = name

#     def show(self):
#         print("Person name:", self.name)


# # Here Child class inheriting Person
# class Student(Person):

#     def __init__(self, name, age):
#         super().__init__(name)     # calling parent constructor
#         self.age = age

#     def show_student(self):
#         print("Student age:", self.age)


# s = Student("Sandy", 10)

# s.show()        
# s.show_student()  

# #method over writting

# class Animal:

#     def sound(self):
#         print("Python is easy")

# class Dog(Animal):

#     def sound(self): 
#         print("I like python")

# d = Dog()
# d.sound()

# #polymorphism

# class Car:

#     def wheel(self):
#         print("I have four wheels")


# class Bike:

#     def wheel(self):
#         print("I have two wheels")


# animals = [Car(), Bike()]

# for a in animals:
#     a.wheel()

# #task

# class Employee:
#     def get_salary(self, s):
#         self.salary = s


# class Manager(Employee):
#     def display(self):
#         print("Manager Salary =", self.salary)


# class Developer(Employee):
#     def display(self):
#         print("Developer Salary =", self.salary)


# class Intern(Employee):
#     def display(self):
#         print("Intern Salary =", self.salary)


# m = Manager()
# d = Developer()
# i = Intern()

# m.get_salary(50000)
# d.get_salary(40000)
# i.get_salary(15000)

# m.display()
# d.display()
# i.display()

# #task2

# class Calculator:

#     def add(self, a, b, c=None):

#         if c is None:
#             return a + b
#         else:
#             return a + b + c


# c = Calculator()

# print("Add two numbers =", c.add(2, 3))
# print("Add three numbers =", c.add(1, 2, 3))
# print('add two decimal =',c.add(2.5,3.5))

# #encapsulation
# # task
# '''       
# class Student:

#     def __init__(self):
#         self.__marks = 0   # private variable

#     def set_marks(self, m):   # public method
#         self.__marks = m

#     def get_grade(self):   # public method
#         if self.__marks >= 90:
#             return "A"
#         elif self.__marks >= 75:
#             return "B"
#         elif self.__marks >= 50:
#             return "C"
#         else:
#             return "Fail"


# s = Student()

# marks = int(input("Enter marks: "))
# s.set_marks(marks)

# print("Grade =", s.get_grade())  

#  #abstraction 
#  # task
# from abc import ABC, abstractmethod


# class Notification(ABC):

#     @abstractmethod
#     def send(self):
#         pass


# class Email(Notification):

#     def send(self):
#         print("Sending Email Notification")


# class SMS(Notification):

#     def send(self):
#         print("Sending SMS Notification")


# class PushNotification(Notification):

#     def send(self):
#         print("Sending Push Notification")


# print("1.Email  2.SMS  3.Push")
# choice = int(input("Enter choice: "))

# if choice == 1:
#     n = Email()

# elif choice == 2:
#     n = SMS()

# elif choice == 3:
#     n = PushNotification()

# else:
#     print("Invalid choice")
#     exit()

# n.send()
# '''

# #class & objects 
# #inheritance

# class Parent:
#     def __init__(self, name):
#         self.name = name

#     def show(self):
#         print("Parent name:", self.name)


# class Child1(Parent):
#     def display(self):
#         print("This is Child1")


# class Child2(Parent):
#     def __init__(self, name, age):
#         super().__init__(name)   # calling parent class
#         self.age = age

#     def display(self):
#         print("Name:", self.name)
#         print("Age:", self.age)


# class Child3(Parent):
#     def display(self):
#         print("This is Child3")


# c1 = Child1("Arun")
# c1.show()

# c2 = Child2("Bala", 22)
# c2.display()

# c3 = Child3("Kumar")
# c3.show()

# #polymorphism

# class Animal:
#     def sound(self):
#         print("Animal sound")


# class Dog(Animal):
#     def sound(self):
#         print("Dog bark")


# class Cat(Animal):
#     def sound(self):
#         super().sound()   # only here super
#         print("Cat meow")


# class Cow(Animal):
#     def sound(self):
#         print("Cow moo")


# d = Dog()
# c = Cat()
# w = Cow()

# d.sound()
# c.sound()
# w.sound()

# #encapsulation

# class Person:

#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age   # private variable

#     def get_age(self):
#         return self.__age

#     def set_age(self, a):
#         self.__age = a


# class Child1(Person):

#     def display(self):
#         print("Child1 Name:", self.name)


# class Child2(Person):

#     def __init__(self, name, age, city):
#         super().__init__(name, age)   # super only here
#         self.city = city

#     def display(self):
#         print("Child2 Name:", self.name)
#         print("Age:", self.get_age())
#         print("City:", self.city)


# class Child3(Person):

#     def display(self):
#         print("Child3 Name:", self.name)


# c1 = Child1("Arun", 20)
# c1.display()

# c2 = Child2("Bala", 22, "Chennai")
# c2.display()

# c3 = Child3("Kumar", 25)
# c3.display()

# #abstraction

# from abc import ABC, abstractmethod


# class Vehicle(ABC):

#     def __init__(self, name):
#         self.name = name

#     @abstractmethod
#     def start(self):
#         pass


# class Bike(Vehicle):

#     def __init__(self, name):
#         super().__init__(name)   # only here super

#     def start(self):
#         print(self.name, "Bike started")


# class Car(Vehicle):

#     def start(self):
#         print("Car started")


# class Bus(Vehicle):

#     def start(self):
#         print("Bus started")


# b = Bike("Yamaha")
# b.start()

# c = Car("BMW")
# c.start()



# #pandas
# #Task 1

# import pandas as pd
# data = {
#      "name": ["John", "Alice", "Bob", "Emma", "David", "Sophia", "Liam"],
#     "age": [30, 25, 35, 28, 40, 22, 31],
#     "city": ["NY", "London", "Sydney", "Paris", "Tokyo", "Berlin", "Dubai"],
#     "salary": [50000, 60000, 55000, 62000, 70000, 48000, 53000]
# }

# df = pd.DataFrame(data)
# #LOC
# print(df.loc[4]) 
# #ILOC
# print(df.iloc[3])

# #UPDATE
# print(df[df["age"] > 35])

# #INSERT
# df["id"] = [52,34,56,76,87,90,12]
# print(df)


# #Task 2
# data = {
#     "Name": ["John", None, None, None],
#     "Age": [25, None, None, None],
#     "City": ["NY", None, None, None]
# }
# df = pd.DataFrame(data)
# #DROPNA
# print(df.dropna())

# #FILLNA
# print(df.fillna(1))

# #Task3
# data = {
#     "Date": ["2025-01-01", "2024-01-02", "2026-01-03", "2023-01-04", "2022-01-05"],
#     "Event": ["Meeting", "Workshop", "Seminar", "Conference", "Webinar"],
#     "Location": ["Chennai", "Delhi", "Mumbai", "Bangalore", "Hyderabad"]
# }

# df = pd.DataFrame(data)
# df["Date"] = pd.to_datetime(df["Date"])
# print(df["Date"].dt.year)
# print(df["Date"].dt.date)
# print(df["Date"].dt.month)

