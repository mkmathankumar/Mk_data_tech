# overridind
class dad:    #parent
    def house(self):
        print('white color house')

class son(dad):     #son
     def factory(self):
        print('yellow color factory')

     def house(self):
         print('blue color house')

s=son()
s.factory()
s.house()

