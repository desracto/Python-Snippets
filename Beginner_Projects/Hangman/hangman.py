from random import randint

# Credit to chrishorton on GitHub for the Hangman Art
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# Credit https://stackoverflow.com/a/13009866
def find_occurrences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]

def get_word_list():
    with open("Beginner_Projects/word_list.txt", "r") as file:
        content_list =  file.readlines()
        content_list = [word.strip() for word in content_list]
        return content_list

def get_man(index):
    if index >= 7:
        return "You have run out of attempts!"
    return HANGMANPICS[index]

def start_game():
    word_list = get_word_list()
    selected_word = word_list[randint(0, len(word_list))]
    CORRECT_WORD = selected_word
    selected_word_guess = ["_" for i in range(0, len(selected_word))]
    error_count = 0
    correct_count = 0

    while True:
      print(selected_word_guess, HANGMANPICS[error_count])
      if error_count == 6:
        print("You've run out of tries! The word was:", CORRECT_WORD)
        break
      if correct_count == len(selected_word):
        print("You got it right!")
        break

      attempt = str(input("Guess a letter: "))
      occurrences = find_occurrences(selected_word, attempt)
      
      if len(occurrences) != 0:
          for i in occurrences:
            selected_word_guess[i] = attempt
            correct_count += 1
          selected_word = selected_word.replace(attempt, "")
          print("Correct guess!") 
      else:
        error_count += 1    
        print("Wrong guess! Attempts remaining: ", len(HANGMANPICS) - error_count - 1)

if __name__ == "__main__":
  game_start = True
  while game_start:
    start_game()
    
    while True:  
      answer = input("Try Again? Y/N ")
      if answer[0].lower() == 'y':
        break
      elif answer[0].lower() == 'n':
        print("Thank you for playing!")
        game_start = False
        break
      else:
        print("Incorrect choice!")

      