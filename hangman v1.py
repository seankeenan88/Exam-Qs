word = ('plants')

index = 0
lives = 2

while lives != 0:
    guess = input('Guess a letter: ')
    found = False
        
    while(not found) and (index != len(word)):
        guess == word[index]
        found = True
        
        print(f'true', index + 1)
        index = index + 1
        lives = lives - 1


        
