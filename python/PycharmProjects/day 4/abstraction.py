from abc import ABC, abstractmethod

class featureplan(ABC):
    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def logout(self):
        pass
                                               #to give @abstractmethod   only this is abstractmethod

class webapp(featureplan):
    def login(self):
        print('webapp login done')
        
    def logout(self):
        print('webapp logout done')


app=webapp()
app.login()
app.logout()