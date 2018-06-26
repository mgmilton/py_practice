#
# Let's import our datafile mpg.csv, which contains fuel economy data for 234 cars.
#
# mpg : miles per gallon
# class : car classification
# cty : city mpg
# cyl : # of cylinders
# displ : engine displacement in liters
# drv : f = front-wheel drive, r = rear wheel drive, 4 = 4wd
# fl : fuel (e = ethanol E85, d = diesel, r = regular, p = premium, c = CNG)
# hwy : highway mpg
# manufacturer : automobile manufacturer
# model : model of car
# trans : type of transmission
# year : model year

import csv


with open('./course1_downloads/mpg.csv') as csvfile:
    mpg = list(csv.DictReader(csvfile))

mpg[:3] # The first three dictionaries in our list
len(mpg) # returns the length of the original dictionary, demonstrating that it is comprised of 234 dictionaries
mpg[0].keys() # returns the column names of our csv

sum(float(d['cty']) for d in mpg) / len(mpg) # This is how to find the average cty fuel economy across all cars

sum(float(d['hwy']) for d in mpg) / len(mpg) # To find the average highway fuel economy across all cars

# Use set to return the unique values for the number of cylinders in the cars in our dataset
cylinders = set(d['cyl'] for d in mpg)
print(cylinders)

# A more complex example where we are grouping the cars by number of cylinder, and finding the average cty mpg for each group

CtyMpgByCyl = []

for c in cylinders: #iterate over all the cylinder levels
    sumpg = 0
    cyltypecount = 0
    for d in mpg: # iterate over all dictionaries
        if d['cyl'] == c: # if the cylinder level type matches
            sumpg += float(d['cty']) # add the cty mpg
            cyltypecount += 1 # increment the count
    CtyMpgByCyl.append((c, sumpg / cyltypecount)) # append the tuple ('chylinder', 'avg mpg')

CtyMpgByCyl.sort(key=lambda x: x[0])
print(CtyMpgByCyl)

#Use set to return the unique values for the class types in our dataset
vehicleclass = set(d['class'] for d in mpg) #what are the class types
vehicleclass

# How to find the average hwy mpg for each class of vehicle in our dataset
HwyMpgByClass = []
for t in vehicleclass: # iterate over all the vehicle classes
    summpg = 0
    vclasscount = 0
    for d in mpg: # iterate over all dictionaries
        if d['class'] == t: # if the cylinder amount type matches,
            summpg += float(d['hwy']) # add the hwy mpg
            vclasscount += 1 # increment the count
    HwyMpgByClass.append((t, summpg / vclasscount)) # append the tuple ('class', 'avg mpg')

HwyMpgByClass.sort(key=lambda x: x[1])
print(HwyMpgByClass)
