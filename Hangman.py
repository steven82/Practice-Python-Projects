import random

def initGame():
	pointsLeft = 6
	words = ['banana', 'stairs', 'books', 'television', 'mouse'
			, 'keyboard', 'feather', 'jacket', 'shoes', 'music']

	# Picks a random word from our list and stores it in 'wordToGuess'
	wordToGuess = random.choice(words)

	# Splits the random word selected into a list of individual characters
	wordToChar = list(wordToGuess)

	# Creates an empty list that is read to be appended with '_'.  This
	# will be our panel that displays the character than the user has 
	# got correct.
	guessPanel = []
	for i in wordToChar:
		guessPanel.append('_')

	# That does it for the initilization of our hangman game, now to call
	# the mainGame() function!
	mainGame(pointsLeft, wordToGuess, wordToChar, guessPanel)

def getUserInput():
	userInput = raw_input('Enter a letter: ') 
	return userInput

def mainGame(pointsLeft, wordToGuess, wordToChar, guessPanel):

	# Main game loop
	while pointsLeft != 0:

		# Checks the selected word against the words that the user has guessed
		# each turn. If the user has guessed all letters then prompt for input.
		if guessPanel == wordToChar:
			print "Congratulations!  The word was: %s" % wordToGuess
			print "You have won! Play again(y/n) "
			if raw_input() == 'y':
				initGame()
			else:
				exit(0)

		# Prints the points left and the 'guessPanel' each turn.  The 'guessPanel'
		# displays how many letters the user has left to guess.
		print 'Turns Left: %d' % pointsLeft
		print guessPanel
		userInput = getUserInput()

		# 'wordtoChar' list is simply a string unpacked into single chars.
		# the .count function checks to see how many time the users input occurs
		# in the list.  As long as it is over zero it will iterate through the list
		# and assign the relevent chars to the 'guessPanel'.  If nothing matches
		# the user will lose one of six points.
		if wordToChar.count(userInput) != 0:
			for i, v in enumerate(wordToChar):
				if userInput == v:
					guessPanel[i] = userInput
		else:
			print "Incorrect!!"
			pointsLeft -= 1
	
	# This occurs when 'pointsLeft' is equal to zero.  
	# Display the word, prompt player for action.
	print "You have run out of points.  The word was: %s" % wordToGuess
	if raw_input("Play again? (y/n) ") == 'y':
		initGame()
	else:
		exit(0)		

# Entry point for the script!
initGame()

