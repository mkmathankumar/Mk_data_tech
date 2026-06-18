class parent:
    def __init__(self):
        self.public_var='public'
        self._protected_var='protected'
        self.__private_var='private'

    def access_from_same_class(self):
        print('inside the parent class:')
        print('public:',self.public_var)
        print('protected:',self._protected_var)
        print('private:',self.__private_var)


class child(parent):

    def access_from_subclass(self):
        print('inside child class (subclass):')
        print('public:',self.public_var)
        print('protected:',self._protected_var)
        try:
            print('private:',self.__private_var)
        except AttributeError:
            print('private: cannot access (attribute error)')

class stranger:

    def access_from_other_class(self,obj):
        print('inside stranger class (unrelated):')
        print('public:',obj.public_var)
        print('protected:', obj._protected_var)
        try:
            print('private:',obj.__privare_var)
        except AttributeError:
            print('private: cannot access (attribute error)')

p = parent()
c = child()
s = stranger()

print('\n acees from same class:')
p.access_from_same_class()
print('\n access from subclass:')
c.access_from_subclass()
print('\n access from other class:')
s.access_from_other_class(p)