# Converts an string from the user to an int, then to a binary string 
# and outputs the answer

def main():
	print "Enter number to convert to binary."
	userInput = raw_input(": ")
	binaryResult == bin(int(userInput))
	print "%s in binary is: %s" % (userInput, binaryResult)

if __name__ == '__main__':
	main()