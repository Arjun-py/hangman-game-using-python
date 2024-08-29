import random


man = [
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


word_list = ["mango", "space", "helicopter", "Coffee", "bicycle", "whale", "Dragon", "pineapple", "guitar", "snowflake"]
live = 6 #initialize the remaining lives
system=random.choice(word_list)  # the system chose random word from the word list


blank =""  
lenth = len(system)

for po in range(lenth):
    blank+="*"
print(blank)

game_over = False
fill = []



while not game_over:
    guess =input("gues a word:").lower()
    display =""
    
    for letter  in system:
        
        if letter==guess:
            display+=letter
            fill.append(letter)
        elif letter in fill:
            display+=letter
        else:
            display+="_"
  
    print(display)
    if guess not in system:
        live-= 1
        
        if live==0:
            game_over = True
            print("you louse")
    
        if "_" not in display:
            game_over = True
            print("you won")
        
      
        print(man[live])