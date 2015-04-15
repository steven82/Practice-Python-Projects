
# Simple to-do list script.  Allows you to record 5 things then recall them
# from a file.

import sys

def mainmenu():
	print "TODO LIST "
	print "****************"
	print "1. New List"
	print "2. Load List"
	print "3. Exit"
	
	userInput = raw_input(prompt)
	if userInput == "1":
		newlist()
	if userInput == "2":
		loadlist()
	if userInput == "3":
		sys.exit(0)

def newlist():

	# Set the current line and get a list/file name from user
	currentLine = 1
	listName = raw_input("Enter a name for the list: ")
	fileName = open(listName, "w")

	# Cast currentLine from and int to a string, numbering the list 
	# and prompt the user for first list item.
	line1 = str(currentLine) + ". " + raw_input("1. ")
	currentLine = currentLine + 1

	line2 = str(currentLine) + ". " + raw_input("2. ")
	currentLine = currentLine + 1

	line3 = str(currentLine) + ". " + raw_input("3. ")
	currentLine = currentLine + 1

	line4 = str(currentLine) + ". " + raw_input("4. ")
	currentLine = currentLine + 1

	line5 = str(currentLine) + ". " + raw_input("5. ")

	# Set lines equal to the five string variables recieved from the user
	# and use \n to seperate them to new lines.
	lines = "%s\n%s\n%s\n%s\n%s\n" % (line1, line2, line3, line4, line5)
	fileName.write(lines)
	fileName.close()
	mainmenu()
	
def loadlist():

	# Get a list name to print from the user, then display it to the console.
	listName = raw_input("Enter the lists name: ")
	fileName = open(listName, 'r')
	print fileName.read()
	mainmenu()

prompt = ">"
mainmenu()
