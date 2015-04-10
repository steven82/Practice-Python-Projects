# Hello! Takes the users name as a command line arguement and displays
# a greeting

import sys

def main():
	print 'Hello, ', sys.argv[1]
	
if __name__ == '__main__':
	main()