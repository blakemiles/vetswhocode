from sys import exit
from random import randint

class Scene(object):

	def enter(self):
		pass


class Engine(object):
	def __init__(self, scene_map):
		self.scene_map = scene_map
		
	def play(self):
		current_scene = self.scene_map.opening_scene()
		last_scene = self.scene_map.next_scene('finished')

		while current_scene != last_scene:
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)

		current_scene.enter()

class Death(Scene):

	quips = [
		"You died. You kinda suck at this.",
		"Your mom would be proud... if she were smarter.",
		"Such a loooooser",
		"I have a small puppy that's better at this"
		"Your an idiot."
	]

	def enter(self):
		print Death.quips[randint(0, len(self.quips))]
		exit(1)

class CentralCorridor(Scene):

	def enter(self):
		print "Stuff"

        action = raw_input("> ")

        if action == "shoot!":
            return 'death'

        elif action == "dodge!":
            print "Like a world class boxer you dodge, weave, slip and slide right"
            print "as the Gothon's blaster cranks a laser past your head."
            print "In the middle of your artful dodge your foot slips and you"
            print "bang your head on the metal wall and pass out."
            print "You wake up shortly after only to die as the Gothon stomps on"
            print "your head and eats you."
            return 'death'

        elif action == "tell a joke":
            print "Lucky for you they made you learn Gothon insults in the academy."
            print "You tell the one Gothon joke you know:"
            print "Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr."
            print "The Gothon stops, tries not to laugh, then busts out laughing and can't move."
            print "While he's laughing you run up and shoot him square in the head"
            print "putting him down, then jump through the Weapon Armory door."
            return 'laser_weapon_armory'

        else:
            print "DOES NOT COMPUTE!"
            return 'central_corridor'

class LaserWeaponArmory(Scene):

	def enter(self):
		print "guess the keypad"
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        guess = raw_input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
        	print "BZZZED"
        	guesses += 1
        	guess = raw_input("[keypad]> ")

        if guess == code:
            return 'the_bridge'
        else:
            print "The lock buzzes one last time and then you hear a sickening"
            print "melting sound as the mechanism is fused together."
            print "You decide to sit there, and finally the Gothons blow up the"
            print "ship from their ship and you die."
            return 'death'


class TheBridge(Scene):

    action = raw_input("> ")

    if action == "throw the bomb":
        print "it goes off."
        return 'death'

    elif action == "slowly place the bomb":
        print "get off this tin can."
        return 'escape_pod'
    else:
        print "DOES NOT COMPUTE!"
        return "the_bridge"

class EscapePod(Scene):

	def enter(self):
		print "You rush through the ship desperately trying to make it to"
        print "the escape pod before the whole ship explodes.  It seems like"
        print "hardly any Gothons are on the ship, so your run is clear of"
        print "interference.  You get to the chamber with the escape pods, and"
        print "now need to pick one to take.  Some of them could be damaged"
        print "but you don't have time to look.  There's 5 pods, which one"
        print "do you take?"

        good_pod = randint(1,5)
        guess = raw_input("[pod #]> ")

        if int(guess) != good_pod:
        	return 'death'
        else:
        	print "You jump into pod %s and hit the eject button." % guess
        	return 'finished'

class Finished(Scene):

    def enter(self):
        print "You won! Good job."
        return 'finished'

class Map(object):

	scenes = {
	    'central_corridor': CentralCorridor(),
	    'laser_weapon_armory': LaserWeaponArmory(),
	    'the_bridge': TheBridge(),
	    'escape_pod': EscapePod(),
	    'death': Death(),
	    'finished': Finished(),
	}

	def __init__(self, start_scene):
		self.start_scene = start_scene

	def next_scene(self, scene_name):
		val = Map.scenese.get(scene_name)
		return val

	def opening_scene(self):
		return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

