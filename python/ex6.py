# string within a string; defining x, binary, and don't
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
# string within a string; string array for multiple export
y = "Those who know %s and those who %s." % (binary, do_not)

# prints x and y
print x
print y

# prints x and y as a string within a string
print "I said: %r." % x
print "I also said: '%s'." % y

# defines hilarious as a boolean False
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# uses string within joke_evaluation string to print hilarious string
print joke_evaluation % hilarious

# defines w and e strings
w = "This is the left side of..."
e = "a string with a right side."

# prints concatenated w and e strings 
print w + e