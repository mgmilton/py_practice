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
