import random

from words import word_list

word=random.choice(word_list)
ur_word=[]
for _ in range(len(word)):
    ur_word.append("_")
game_is_on=True
lives=6
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo)

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

def check(string):
    if string in word:
        return True

def print_word(letter):
    for i in range(len(word)):
        if(letter==word[i]):
            ur_word[i]=letter
    print(" ".join(ur_word))

while game_is_on:
    n=input("Enter a letter")
    if check(n)==True:
        print_word(n)
    else:
        print(stages[lives])
        lives-=1
    l=' '.join(ur_word)
    if "_"  in ur_word and lives==-1:
        game_is_on=False
        print(f"You lost, the word was {word}")
    elif "_" not in ur_word and lives>-1:
        print("You won!!")
        game_is_on=False


