def add_numbers(x,y):
    return x + y

type('This is a string')
type(None)
type(1)
type(1.0)
type(add_numbers)

# Tuples are an immutable data structure
x = (1, 'a', 2, 'b')
type(x)

# Lists are a mutable data structure
x = [1, 'a', 2, 'b']
type(x)

# Use append to add an objec to the end of a list
x.append(3.3)
print(x)

# This is an example of how to loop through each item in the list
for item in x:
    print(item)

# Using the indexing operator:
i = 0
while( 1 != len(x) ):
    print(x[i])
    i = i + 1


# How to concatenate lists
[1,2] + [3,4]

# Use * to repeate lists
[1]*3

# Use the in operator to check if something is inside a list
1 in [1, 2, 3]
