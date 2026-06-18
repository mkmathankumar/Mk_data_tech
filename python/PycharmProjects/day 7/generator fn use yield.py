def get_number(n):
    return [i for i in range(n)]

print(get_number(10))

def gets_number(n):
    for i in range(n):
        yield i

for num in gets_number(5):
    print(num)