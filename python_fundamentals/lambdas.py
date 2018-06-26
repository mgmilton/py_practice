# an example of lambda that takes three parameters and adds the first two
my_function = lambda a, b, c : a + b
my_function(1,2,3)

# iterate through 0 to 999 returning only the even numbers
my_list = []
for number in range(0, 1000):
    if number % 2 == 0:
        my_list.append(number)
my_list

# same iteration but with list comprehension

my_list = [number for number in range(0, 1000) if number % 2 == 0]
my_list
