# Question 16(b)
# Examination Number:

# A variable to store all the lower case letters in the alphabet
LOWER_CASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'

def calculate_score(password):
    
    # the variable lowercase and uppercase indicate the presence
    # or absence of lowercase and uppercase characters in the password
    lowercase = False # True if password contains a lowercase letter
    uppercase = False # True if password contains an uppercase letter
    
    # Loop through each charactyer in the password and ...
    # ... check the password for specific characters
    for character in password:
        if character in LOWER_CASE_LETTERS:
            lowercase = True
        if character in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            uppercase = True
            
    # calculate score based on rules
    
    score = 0
    
    # Rule 1
    if len(password) > 7:
        score = score + 5
        
    # Rule 2
    if lowercase:
        score = score + 1
        
    # Rule 3
    if lowercase and uppercase:
        score = score + 5
        
    return score

def is_strong(password):
    return(calculate_score(password) == 11)

# Test driver
test_passwords = ['sun', 'Sun', 'Sunshine', '12345', 'Moonlight']
print('Score\tPassword','\n-----\t--------')
for password in test_passwords:
    pass_score = calculate_score(password)
    print(pass_score, '\t', password)
    lowest_score = 999
    weakest_password = ''
        
for password in test_passwords:
    pass_score = calculate_score(password)
    if pass_score < lowest_score:
        lowest_score = pass_score
        weakest_password = password
    print(pass_score,'\t',password)
    
print()
print('The weakest password is:',weakest_password)
print('Score:',lowest_score)
print()
print('The strong passwords are:')
for password in test_passwords:
    if is_strong(password):
        print(password)