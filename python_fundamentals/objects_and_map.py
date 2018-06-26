# an example of a class in python

class Person:
    job = 'community organizer' #a class variable

    def set_name(self, new_name): #a method
        self.name = new_name


    def set_location(self, new_location):
        self.location = new_location


person = Person()
person.set_name('Barack Obama')
person.set_location('Hyde Park Chicago, IL, USA')
print('{} lives in {} and works as a {}.'.format(person.name, person.location, person.job))


#an example of mapping the min function between two lists
store1 = [10.00, 11.00, 12.34, 2.34]
store2 = [9.00, 11.10, 12.34, 2.01]
cheapest = map(min, store1, store2)
cheapest

for item in cheapest:
    print(item)
