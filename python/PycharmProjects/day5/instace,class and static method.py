class employee:
    company='open ai'

    @classmethod
    def change_commpany(cls,new_name):
        cls.company=new_name

    @staticmethod             #static method only change in their funcion only then not change other classes
    def try_change_new_name(new_name):
        company=new_name

employee.change_commpany('google')
print('after class method:',employee.company)

employee.try_change_new_name('meta')
print('after static method:',employee.company)