class Human:
     ## Atributes or Properties
    number_of_legs = 0
    number_of_hands = 0
    energy = 0
    mouth = 0
    jumping_ability = False
    number_of_ears = 0
    eyes = 0
    name = ""
    nostril = 0

# Constructor
    def __init__(self,name,eyes,number_of_legs,number_of_hands,number_of_ears,mouth):
        self.name = name
        self.eyes = eyes
        self.number_of_legs = number_of_legs
        self.number_of_hands = number_of_hands
        self.number_of_ears = number_of_ears
        self.mouth = mouth

    def clap(self):
        available_hands = self.number_of_hands
        return f"clapping with {available_hands} hands"

    

stan = Human("stan", 2, 2, 2, 2, 1)
dice = Human("dice", 2, 2, 2, 2, 1)
print(stan.name)
print(f"{stan.name} is {stan.clap()}")
print(f"{dice.name} is {dice.clap()}")
print(type(stan))
print(stan.clap())