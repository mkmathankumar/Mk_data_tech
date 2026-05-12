class employee:
    def __init__(self,name,aadhar):
        self.name=name
        self.aadhar=aadhar

    def enter_office(self):
        print(f'{self.name} enter using aadhar {self.aadhar}.')

    def open_bank_account(self):
        print(f'bank account opened for {self.name} with aadhar {self.aadhar}.')

emp1=employee('mkmatahn','1234-5678-9012')
emp1.enter_office()
emp1.open_bank_account()