#imports argv module
from sys import argv

#applies variables to argv module
script, input_file = argv

#defines print_all function to f variable to print read
def print_all(f):
  print f.read()

#returns read function to the 0th byte of the file
def rewind(f):
  f.seek(0)

#defines print_a_line function to count the lines of a file
def print_a_line(line_count, f):
  print line_count, f.readline()

#assigns current_file variable to opening the input_file
current_file = open(input_file)

#prints print_all function which reads file f
print "First let's print the whole file:\n"

print_all(current_file)

#calls rewind function and sets current file to byte 0
print "Now let's rewind, kind of like a tape."

rewind(current_file)

#prints current line from current file with current_line \
#variable being applied through the line_count variable in \
#print_a_line function; then each line adds one line
print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
