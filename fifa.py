import random

class Human:
    # Constructor
    def __init__(self,name,age,face, height):
        self.name = name
        self.age = age
        self.face = face
        self.height = height
        self.accessories = 0
        self.hands = 2
        self.mouth = 1
        self.eyes = 2
        self.ears = 2
        self.legs = 2
        self.head = 1
        self.weight = 0
        self.accessories = 0 
        self.complexion = ""
        self.mood = ""
    
    #define the various actions that are going to take place through out the match
    def walk(self):
        return "walking"
   
    def heading(self):
        return "heading"
    
    def dribble(self):
        return "dribbling"
    
    def juggle(self):
        pass




class Player(Human):

    # Constructor
    def __init__(self, name, age, face, height, boots, jersey_number, mood, celebration, jersey_colour, physique, hairstyle):
        super().__init__(name, age, face, height)
        self.boots = boots
        self.jersey_number = jersey_number
        self.mood = mood
        self.celebration = celebration
        self.jersey_colour = jersey_colour
        self.physique = physique
        self.hairstyle = hairstyle

class Chelsea(Player):
    def __init__(self, name, age, face, height, boots, jersey_number, mood, celebration,  physique, hairstyle):
        super().__init__(self, name, age, face, height, boots, jersey_number, mood, celebration,  physique, hairstyle)
        self.jersey_colour = "blue"
        self.logo = "lion"




player2 = Player("Fred", 22,"round", 185, 2, 23, "Happy", "Scream", "pink", "Slim", "waves")
print(player2.jersey_colour)
print(player2.name)
# caicedo = Chelsea("Caicedo",20,"black", 185, "nike",23,"happy","hug","fit","low cut")
# print(caicedo.name)