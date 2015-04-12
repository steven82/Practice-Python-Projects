# Random Name Generator 

import random

print 'Random Name Generator\n\n'

# Arrays that hold the different name sections.
firstNames = ['Steven', 'Alan', 'Craig', 'Billy', 'Scott', 'Adam', 'Robert', 'Indiana', 'Eddie', 'Chris']
middleNames = ['Bob', 'Shug', 'Dee', 'Gerry', 'Bill', 'Donald', 'Han', 'Luke', 'Ben', 'Al']
lastNames = ['Wisniewski', 'Honey', 'Farris', 'Gorman', 'Williams', 'Dennis', 'Hendricks', 'Lenny', 'McKay', 'Rotham']

# The following code selects a listed item at random then prints it to the console
a, b, c = random.choice(firstNames, middleNames, lastNames)
print '%s %s %s' % (a, b, c)