def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(6))

def countdown(n):
    if n == 0:
        print('boom')
        return
    print(n)
    countdown(n-1)

print(countdown(10))