#l-local variable
def order():
    food="curd rise"
    print("your order is:",food)

order()

#E-enclosing
def card():
    discount=10

    def checkout():
        print("applying discount:",discount)

    checkout()

card()

#G-global
user_id="mkmathan"

def homepage():
    print("welcome:",user_id)
def profile():
    print("welcome to the profile page:",user_id)

homepage()
profile()

#B-build in
print(__file__)

#usecase
delivery_partner="swiggy"

def hotel():
    item="pizza"

    def ordernow():
        quantity=2
        print(f"ordering {quantity} {item} using {delivery_partner}")
    ordernow()

hotel()