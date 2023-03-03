import random

words ={'table', 'chair', 'pen', 'pencil'}

word = random.choice(words)
length = len(word)
count = 0
display = '_ ' * length

guess = input('This is your word: ' + display + 'Please enter your guess: ')
if len(guess) == 0 or len(guess) >= 2:
    print('Invalid entry, please guess one letter')
    
if guess in word:
    print('Congrats', guess, 'is in this word')
    
    elif guess not in word
    print('Your guess is incorrect')
    
    