from sys import exit
from random import randint
from textwrap import dedent

#CLASS MAP
class Map(object):
    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass

#CLASS ENGINE
class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # imprima a última cena
        current_scene.enter()

#CLASS SCENE
class Scene(object):
    def enter(self):
        print('this scene is not configured yet')
        print('subclass it and implement enter().')
        exit(1)

#CLASS SCENE - Derivados
class Death(Scene):
    quips = [
        "you died. You kinda suck at this",
        "Your mom would be proud.. if she were smarter",
        "Such a looser",
        "I have a small puppy that's better at this.",
        "You're worse than your Dad's jokes"
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class Central_Corridor(Scene):
    def enter(self):
        print(dedent("""
        The Gothons of Planet Percal #25 have invaded your ship and destroyed your entire crew.  You are the last surviving member and your last mission is to get the neutron destruct bomb from the Weapons Armory, put it in the bridge, and blow the ship up after getting into an escape pod.
         
         You're running down the central corridor to the Weapons Armory when a Gothons jumps out, red scarly skin, dark grimy teeth, and evil clown costume flowing around his hate filled body. He's blocking the door to the Armory and about to pull a weapon to blast you"""))

        action = input('> ')

        if action == "shoot!":
            print(dedent("""
                Quick on the draw you yank out  your blaster and fire it at the Gothon. His clown costume is flowing and moving around his body, which throw off your aim. Your laser hits his costume but misses him entirely. This completely ruins his brand new costume his mother bought him, which makes him fly into an insane rage and blast you repeatedly in the face until you are dead. Then he eats you. """))
            return 'death'
        elif action == 'dodge!':
            print(dedent("""
                Like a world class boxer you dodge, weave, slip and slide right as the Gothons's blaster cranks a laser past your head. In the middle of your artful dodge your foot slips and you bang your head on the metal wall and pass out. You wake up shortly after only to die as the Gothons stomps on your head and eats you. """))
            return 'death'

        elif action == 'tell a joke':
            print(dedent("""
                Lucky for you they made you learn Gothon insults in the academy. You tell the one Gothon joke you know:
                Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr. The Gothon stops, tries not to laugh, then busts out laughing and can't move. While he's laughing you run up and shoot him square in the head putting him down, then jump through the Weapon Armory door. """)
class Laser_Weapon_Armory(Scene):
    def enter(self):
        pass

class The_Bridge(Scene):
    def enter(self):
        pass

class Escape_Pod(Scene):
    def enter(self):
        pass

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

