name = 'Zed A. Shaw'
age = 35 
height = 74 #inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair. " % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
	age, height, weight, age + height + weight)
	
# conversion to metric
centmtr = height * 2.54
kilo = weight * 0.453592
print "The following measurements are have been converted to metric:"
print "Height: %d cm" % centmtr
print "Weight: %d kg" % kilo

print "Print this no matter what -- %r" % name