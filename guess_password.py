# Simple python script to practice file I/O
# 
#

# Get a password from the user and compare it with thwe stored password
password = raw_input('Enter the password: ')

# Opens a file for appending. if the file does not exists, one is created.
f = open("password.txt", "a")

# Opens the same file for reading only.
f = open("password.txt", "r")

# Get the string from the file and pass it to a variable
stored_password = f.read()

# Make sure the correct password was entered
if password == stored_password:
	print 'Password Accepted'
	answer = raw_input('Would you like to change password? (y/n) ')

	# Get new password from the user and write it to a txt file
	if answer == 'y':
		new_password = raw_input('Enter new password: ')
		f = open("password.txt", "w")
		f.write(new_password)
		f.close
		print 'New password accepted..'

else:
	print 'Wrong Password.'