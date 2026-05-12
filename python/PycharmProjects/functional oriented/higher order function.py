#normal higher order function
def build_email(username,provider):
    if provider == 'gmail':
        return f'{username}@gmail.com'
    elif provider == 'ymail':
        return f'{username}@ymail.com'
    elif provider == 'hotmail':
        return f'{username}@hotmail.com'
    else:
        return f'{username}@example.com'


print(build_email('mkmath','gmail'))
print(build_email('rahul','ymail'))
print(build_email('gokul','hotmail'))
print(build_email('john','unknown'))


