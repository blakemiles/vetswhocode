#imports the argv function from the command line call
from sys import argv

#applies variable names to argv variable
script, filename = argv

#applies the function of open(filename) to the txt variable
txt = open(filename)

#prints filename and prints the filename from txt variable in read format
#print "Here's your file %r:" % filename
#print txt.read()

#asks for the filename to apply to the file_again variable
#print "Type the filename again:"
file_again = raw_input("> ")

#applies the filename from file_again to be opened when txt_again is called
txt_again = open(file_again)

# prints the file from file_again to a read format
print txt_again.read()


