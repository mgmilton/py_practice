def add_numbers(x, y):
    return x + y

print(add_numbers(1, 2))

# add_numbers updated to take an optional 3rd parameter

def add_numbers(x, y, z=None):
    if (z==None):
        return x + y
    else:
        return x + y + z

print(add_numbers(1,2))
print(add_numbers(1,2,5))


## add_numbers updated to take an optional flag parameter

def add_numbers(x, y, z=None, flag=False):
    if(flag):
        print('Flag is true!')
    if(z==None):
        return x + y
    else:
        return x + y + z

print(add_numbers(1, 2, flag=True))

def add_numbers(x,y):
    return x + y

a = add_numbers
print(a(1,2))
