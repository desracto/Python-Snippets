# Super basic Rock paper scissors game in python

from random import randint
CHOICES = [1, 2, 3]
# R P S

def convert_move(move):
    if move == "r":
        return 1
    if move == "p":
        return 2
    if move == "s":
        return 3

def determine_winner(player_move: str, computer_move: str):
    # Rock
    if player_move == 1 and computer_move == 2:
        return "Computer"
    if player_move == 1 and computer_move == 3:
        return "Player"
    if player_move == 1 and computer_move == 1:
        return "Draw"
    
    # Paper
    if player_move == 2 and computer_move == 3:
        return "Computer"
    if player_move == 2 and computer_move == 1:
        return "Player"
    if player_move == 2 and computer_move == 2:
        return "Draw"
    
    # Scissiors
    if player_move == 3 and computer_move == 1:
        return "Computer"
    if player_move == 3 and computer_move == 2:
        return "Player"
    if player_move == 3 and computer_move == 3:
        return "Draw"

def start_game():
    player_score = 0
    computer_score = 0
    while True:
        print("Player Score: ", player_score, "| Computer Score:", computer_score)
        player_move = int(input("What is your move? 1. Rock, 2. Paper, 3. Scissors, 9. Exit | Choice: "))
        if player_move == 9:
            break
        if player_move not in [1, 2, 3]:
            print("Incorrect input! Try again")
            continue
        
        computer_move = CHOICES[randint(0, 2)]
        winner = determine_winner(player_move, computer_move)
        if winner in ["Player", "Computer"]:
            if winner == "Player":
                print("Player wins!")
                player_score += 1
            else:
                print("Computer Wins!")
                computer_score += 1
        else:
            print(winner)


if __name__ == "__main__":
    start_game()

