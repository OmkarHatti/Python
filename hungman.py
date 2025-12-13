import random
stages=['''
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
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''',r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
Dead  |
=========''']
word_list = {
    "polymorphism": "Ability of different objects to respond to the same method in different ways.",
    "recursion": "A function that calls itself to solve a problem.",
    "encapsulation": "Bundling data and methods together while restricting direct access.",
    "deadlock": "A situation where processes wait forever for resources.",
    "abstraction": "Showing only essential features and hiding implementation details."
}
keys=list(word_list.keys())
stage_count=0
random_choice=random.choice(keys)
print(f"Hint:-{word_list[random_choice]}")

string=''
for i in range(len(random_choice)):
    string+="_"
print(string)
print(stages[stage_count])
full=False

correct_list=[]

while  not full:
    display=''
    guess=input("Guess letter:").lower()
    if guess in random_choice:
        for letter in random_choice:
            if guess==letter:
                display+=letter
                correct_list.append(guess)
            elif letter in correct_list:
                display+=letter
            else:
                display+='_'
        print(display)
        print(stages[stage_count])
    else:
        print("Wrong")
        stage_count+=1
        print(stages[stage_count])
        if stage_count==7:
            print("You loose")
            break
        continue
    
    if '_' not in display:
        print("You did it")
        full=True