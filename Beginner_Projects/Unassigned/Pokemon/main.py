from Pokemon import *
from Game_Engine import *

if __name__ == "__main__":
    move1 = Pokemon.generate_move_map("Fireball", 50, 0.75)
    move2 = Pokemon.generate_move_map("Bite", 1000, 0.05)
    charizard = Pokemon("Charizard", [move1, move2])

    move3 = Pokemon.generate_move_map("Thunderolt", 100, 0.5)
    move4 = Pokemon.generate_move_map("Heart Stop", 100000, 0.01)
    pikachu = Pokemon("Pikachu", [move3, move4])

    print(Game.determine_winner_output(charizard.moves[1], pikachu))

