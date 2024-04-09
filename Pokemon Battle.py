print ("Welcome to Pokemon Stadium!")
class Pokemon:
    def __init__(self, name, level=1, health=100, pokemon_type="Normal" ):
        self.name = name
        self.level = level
        self.health = health
        self.pokemon_type = pokemon_type
    def attack(self, attackee):
        print(self.name, "Attacks",attackee.name )
        attackee.health = attackee.health - 10
    def speak(self):
        print("Pokemon sound")
        
    def __str__(self):
        return "Pokemon: {}".format(self.name)



class Pikachu(Pokemon):
    def __init__(self):
        super().__init__("Pikachu")
        self.type = "Electric"
    def attack(self, attackee):
        attackee.health -=10;
        print ("Pikachu uses thunderbolt on ", attackee.name)
    def speak(self):
        print ("Pika.. Pika.. Pikachu!")


    

class Bulbasaur(Pokemon):
    def __init__(self):
        super().__init__("Bulbasaur")
    def attack(self, attackee):
        attackee.health -= 10;
        print ("Bulbasaur uses razor leaf on ", attackee.name)
    def speak(self):
        print ("Bulba.. Bulba.. Bulbasaur!")
    
class Stadium():
    def __init__(self, name, pokemon_a, pokemon_b):
        self.name = name
        self.pokemon_a = pokemon_a
        self.pokemon_b = pokemon_b
    def battle(self):
        self.pokemon_a.speak()
        self.pokemon_b.speak()
        while self.pokemon_a.health > 0 and self.pokemon_b.health > 0:
            print (f"{self.pokemon_a.name} health : {self.pokemon_a.health}")
            print (f"{self.pokemon_b.name} health : {self.pokemon_b.health}")
            self.pokemon_a.attack(self.pokemon_b)
            if self.pokemon_b.health <= 0:
                break
            self.pokemon_b.attack(self.pokemon_a)
            if self.pokemon_a.health <= 0:
                break

        if self.pokemon_a.health > 0:
            print (f"{self.pokemon_a.name} wins!")
        else:
            print (f"{self.pokemon_b.name} wins!")


pikachu = Pikachu()
bulbasaur = Bulbasaur()
stadium = Stadium("Pokemon Stadium", pikachu, bulbasaur)
stadium.battle()
        

