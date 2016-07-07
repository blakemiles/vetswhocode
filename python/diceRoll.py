#This app will do the following:
# randomly roll dice pair
# add values of roll
# ask user to guess value
# compare user guess to actual
# decide winner
# inform user who won

from random import randint
from time import sleep

def get_user_guess():
  user_guess = int(raw_input("What number do you guess the die will land on? "))
  return user_guess

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print "The maximum possible value is: " + str(max_val)
  sleep(1)
  user_guess = get_user_guess()
  if user_guess > max_val:
    print "Guess invalid"
    return
  else:
    print "Rolling..."
    sleep(2)
    print "First roll: %d" % first_roll
    sleep(1)
    print "Second Roll: %d" % second_roll
    sleep(1)
    total_roll = first_roll + second_roll
    print "Result: %d" % total_roll
    sleep(1)
    if user_guess > total_roll:
      print "You won with a guess of %d!" % user_guess
      return
    else:
      print "Sorry, your guess of %d lost" % user_guess
      return
  
roll_dice(12)