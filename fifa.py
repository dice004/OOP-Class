import random

class Human:
    # Constructor
    def __init__(self,name,age,face, height):
        self.name = name
        self.age = age
        self.face = face
        self.height = height
        self.hands = 2
        self.mouth = 1
        self.eyes = 2
        self.ears = 2
        self.legs = 2
        self.head = 1
        self.weight = 0
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




class Chelsea_Player(Human):

    # Constructor
    def __init__(self, name, age, face, height, boots, jersey_number, mood, celebration, physique, hairstyle):
        super().__init__(name, age, face, height)
        self.boots = boots
        self.jersey_number = jersey_number
        self.mood = mood
        self.celebration = celebration
        self.jersey_colour = "Blue"
        self.physique = physique
        self.hairstyle = hairstyle
        self.logo = "Lion"

class Barca_Player(Human):

    def __init__(self, name, age, face, height, boots, jersey_number, mood, celebration,  physique, hairstyle):
        super().__init__(name, age, face, height)
        self.boots = boots
        self.jersey_number = jersey_number
        self.mood = mood
        self.celebration = celebration
        self.jersey_colour = "Red & Blue"
        self.physique = physique
        self.hairstyle = hairstyle
        self.logo = "Catalonia"




player2 = Barca_Player("Pique", 35, "round", 195, 2, 5, "happy", "Sream", "Tall","wavy")
print(player2.jersey_colour)
print(player2.name)
caicedo = Chelsea_Player("Caicedo",20,"black", 185, "nike",23,"happy","hug","fit","low cut")
print(caicedo.name)