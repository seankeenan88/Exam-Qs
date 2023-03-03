# Question 16(a)
# Examination Number:

# Prompt the user to enter a password and store the ...
# value entered in the variable password
password = input("Enter a password: ")

# A variable to store all the lowercase letters in the alphabet
LOWER_CASE_LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPER_CASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWZYX"
DIGITS = '0123456789'
# The variables lowercase and uppercase indicate the presence or ...
# absence of lowercase and uppercase characters in the password
lowercase = False # True if password contains a lowercase letter
uppercase = False # True if password contains an uppercase letter
digit = False # True if password contains a digit

# Loop through each character in the password and ...
# check the password for specific characters
for character in password:
    if character in LOWER_CASE_LETTERS:
        lowercase = True
    if character in UPPER_CASE_LETTERS:
        uppercase = True
    if character in DIGITS:
        digit = True 

# Calculate the score based on the rules

# initialise score 
score = 0

# Rule 1
if len(password) > 7:
    score = score + 5
    
elif len(password) <4>7:
    score = score + 2
    
elif len(password) < 4:
    score = score - 2

# Rule 2
if lowercase:
    score = score + 1
    
# Rule 3
if lowercase and uppercase:
    score = score + 5

# Rule 4
if uppercase:
    score = score + 2 

# Rule 5
if digit:
    score = score + 5
    
# Rule 6
last = len(password) - 1

if password[0] == digit:
    score = score + 1
    
if password[last] in DIGITS:
    score = score + 2
    
if password[last] and password[0] in DIGITS:
    score = score + 2
    
# Rule 7
if password.isdigit():
    score = score - 10
    

# Display the score
print('Password: ',password)
print('Score: ',score) 