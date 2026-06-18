def outer(msg):
    def inner():
        return (f'message is:{msg}')
    return inner

say_hi =outer('vanakkam da mappilai')
print(say_hi())