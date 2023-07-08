from Pokemon import Pokemon
from random import randint

class Game():
    def determine_winner_output(self, move1: map, player2: Pokemon):
        move1_hit_chance = randint(0, 1)
    
        if move1_hit_chance <= move1["accuracy"]:
            player2.health = player2.health - move1["damage"]
            print("Hit!", player2.name , " health reduced to: ", player2.health)
        else:
            print(move1["name"], "missed!", player2.name, "still at", player2.health, " health!")
