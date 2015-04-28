# This script takes a command-line arguement and counts how many letters 
# are in the given string.
#

import sys

def main(userName, count):
	for i in userName:
		count += 1
		print "%s is letter No.%d" % (i, count)
	print "There are %d letters in total here!\n" % count

if __name__ == '__main__':
	count = 0
	try:
		main(sys.argv[1], count)
	except:
		print "Error!  Enter word as command-line arguement!"
		print "Usage: python word_count.py -wordtocount-"