# Random Name Generator 

import random

print 'Random Name Generator\n\n'

# Arrays that hold the different name sections.
firstNames = ['Steven', 'Alan', 'Craig', 'Billy', 'Scott',
			  'Adam', 'Robert', 'Indiana', 'Eddie', 'Chris',
			  'Ainsley', 'Wade','Walden', 'Nadine', 'Napoleon']

middleNames = ['Bob', 'Shug', 'Dee', 'Gerry', 'Bill', 
			   'Donald', 'Han', 'Luke', 'Ben', 'Alfonzo',
			   'Naozumi', 'Gabe', 'Jack', 'Eadric', 'Wagner']

lastNames = ['Wisniewski', 'Honey', 'Farris', 'Gorman', 'Williams',
			 'Dennis', 'Hendricks', 'Lenny', 'McKay', 'Rotham',
			 'Daniels', 'Glen', 'Kane', 'Patterson', 'Mahaney']

# The following code selects a listed item at random then prints it to the console

a = random.choice(firstNames)
b = random.choice(middleNames)
c = random.choice(lastNames)

print '%s %s %s' % (a, b, c)