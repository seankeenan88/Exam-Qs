# Question 16(a)
 # Examination Number:

from random import randint  

print("Dice simulation and analysis program")
results = [] # initiating the variables 
frequencies = [0, 0, 0, 0, 0, 0] 

 # Loop 100 times
for i in range (100):
    throw_result = randint(1,6) # store a random value between 1 and 6
    results.append(throw_result) # append each value to results
    
# Start to build up a list of frequencies for each value thrown
    if throw_result == 1:
        frequencies[0] = frequencies[0] + 1
    elif throw_result == 2:
        frequencies[1] = frequencies[1] + 1
    elif throw_result == 3:
        frequencies[2] = frequencies[2] + 1
    elif throw_result == 4:
        frequencies[3] = frequencies[3] + 1
    elif throw_result == 5:
        frequencies[4] = frequencies[4] + 1
    elif throw_result == 6:
        frequencies[5] = frequencies[5] + 1
    
        

print()
#print('Results:', results)
print('Frequencies:', frequencies)

print('Dice Frequency')
print('---- ---------')

print('1   ',frequencies[0])
print('2   ',frequencies[1])
print('3   ',frequencies[2])
print('4   ',frequencies[3])
print('5   ',frequencies[4])
print('6   ',frequencies[5])
 
alist = [frequencies[1],frequencies[2],frequencies[3],frequencies[4],frequencies[5]]
if frequencies[0] == max(alist):
    a = '1'
elif frequencies[1] == max(alist):
    a = '2'
elif frequencies[2] == max(alist):
    a = '3'
elif frequencies[3] == max(alist):
    a = '4'
elif frequencies[4] == max(alist):
    a = '5'
elif frequencies[5] == max(alist):
    a = '6'

top = max(alist)
print('')
print(a, 'was rolled most often -', top)

print()
for freq in frequencies
for i in range(freq):
    print('*', end='')
print()



    
  
    
    
    
    
    
    
    
    
    
