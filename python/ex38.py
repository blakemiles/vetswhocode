ten_things = "apples oranges crows telephone light sugar"

print "Wait there are not 10 things in that list. lets' fix that"

stuff = ten_things.split(' ')
more_stuff = ["day", "night", "song", "frisbee", "corn", "banana", "girl", "boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print "adding: ", next_one
	stuff.append(next_one)
	print "There are %d items now." % len(stuff)

print "there we go: ", stuff

print "lets do some things with stuff"

print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)
print '#'.join(stuff[3:5])