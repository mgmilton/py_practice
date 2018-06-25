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
# i = 0
# while( 1 != len(x) ):
#     print(x[i])
#     i = i + 1


# How to concatenate lists
[1,2] + [3,4]

# Use * to repeate lists
[1]*3

# Use the in operator to check if something is inside a list
1 in [1, 2, 3]

#Strings
x = 'This is a string'
print(x[0]) # returns first character
print(x[0:1]) #first character, but we have explicitly set the end character
print(x[0:2]) #first two characters

#This will return the last element of the string
x[-1]
#This will return the slice starting from the 4th element from the end and stopping before the 2nd element from the end
x[-4:-2]
#This is a slice from the beginning of the string and stopping before the 3rds element.
x[:3]
#And this is a slice starting from the 4th element of the string and going all the way to the end
x[3:]


firstname = 'Christopher'
lastname = 'Brooks'

print(firstname + ' ' + lastname)
print(firstname*3)
print('Chris' in firstname)

#split returns a list of all the words in a string or a list split on a specific character
firstname = 'Christopher Arthur Hansen Brooks'.split(' ')[0] # [0] selects the first element of the list
lastname = 'Christopher Arthur Hansen Brooks'.split(' ')[-1] # [0] selects the last element of the list
print(firstname)
print(lastname)

# 'Chris' + 2
print('Chris' + str(2))

# Dictionaries associate keys with values

x = {'Christopher Brooks': 'brooksch@umich.edu', 'Bill Gates': 'billg@microsoft.com'}
x['Christopher Brooks'] # Retrieve a value by using the indexing operator

x['Roscoe'] = None
x['Roscoe'] # nothing is returned

# Iterating over all of the keys
for name in x:
    print(x[name])

# Iterating over all of the values:
for email in x.values():
    print(email)

# Iterating over all of the items in the list:
x = {'Christopher Brooks': 'brooksch@umich.edu', 'Bill Gates': 'billg@microsoft.com'}
for name, email in x.items():
    print(name)
    print(email)

#Upnacking a sequence into different variables:
x = ('Christopher', 'Brooks', 'brooksch@umich.edu')
fname, lname, email = x
print(fname)
print(lname)
