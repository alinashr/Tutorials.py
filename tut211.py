# Custom Exception : Python tutorial 211
# Q: Why custom exception??
# A: To increase the readability of code.

class nametooshort(ValueError):
    pass

def validate(name):
    if len(name)<8:
        raise nametooshort('name is too short')

username=input('Enter your name: ')
validate(username)
print(f'hello {username}')















