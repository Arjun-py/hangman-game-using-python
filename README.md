import random

HANGMANPICS = [
'''
 +---+
 |   |
 O   |
 /|\  |
 / \  |
 =========
 ''','''
 +---+
 |   |
 O   |
 /|\  |
     |
 =========
 ''','''
 +---+
 |   |
 O   |
 /|   |
     |
 =========
 ''','''
 +---+
 |   |
 O   |
 |   |
     |
 =========
 ''','''
 +---+
 |   |
 O   |
     |
     |
 =========
 ''','''
 +---+
 |   |
     |
     |
     |
 =========
 ''']


word_list = ["mango", "space", "helicopter", "coffee", "bicycle", "whale", "dragon", "pineapple", "guitar", "snowflake"]
live = 6
system = random.choice(word_list)
print(system)  # You might want to remove this in the actual game

blank = ""
length = len(system)

for _ in range(length):
    blank += "*"
print(blank)

game_over = False
fill = []

while not game_over:
    guess = input("Guess a word: ").lower()

    display = ""

    for letter in system:
        if letter == guess:
            display += letter
            fill.append(letter)
        elif letter in fill:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in system:
        live -= 1
        if live == 0:
            game_over = True
            print("You lose")
            print(f"The word was: {system}")
    
    if "_" not in display:
        game_over = True
        print("You won")

    if live >= 0:
        print(HANGMANPICS[live])
# hangman-game-using-python
