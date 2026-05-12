# example 1
class student:

    def say_hello(self):
        print('hi,i am a student')

s1=student()
s1.say_hello()

# exampl2

class students:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade

    def display(self):
        print(f"{self.name} is in grade {self.grade}")

a1=students('mk',11)
a2=students('mathan',6)
a3=students('vijay',18)

a1.display()
a2.display()
a3.display()

