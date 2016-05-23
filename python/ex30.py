people = 3021
cars = 401
trucks = 1522


if cars > people:
  print "We should take the cars."
elif cars < people:
  print "We should not take the cars."
else:
  print "We cant decide."

if trucks > cars:
  print "Thats too many trucks."
elif trucks < cars:
  print "Maybe we could take the trucks."
else:
  print "We still can't decide."

if people > trucks:
  print "Alright, lets jsut take the trucks"
else:
  print "Fine, lets stay home then."

