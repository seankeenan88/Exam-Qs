#funtion defintion used in part (v)
def is_anagram(w1,w2):
    if sorted(w1) == sorted(w2):
        return True
    else:
        return False
   
word1 = input("Enter the first word:").lower()
word2 = input("Enter the second word:").lower()



# test whether the sorted strings are the same as each other
# if the sorted strings are the same then they must be anagrams

if (sorted(word1) == sorted(word2)):
    print (word1, "is an anagram of", word2)
else:
    print (word1, "is not an anagram of", word2)
if (sorted(word1) == sorted(word2)):
    print (word1, "is an anagram of", word2)
else:
    print (word1, "is not an anagram of", word2)

word3 = input('Enter a phrase: ')

if (sorted(word1) == sorted(word3)):
    print (word1, "is an anagram of", word3)
else:
    print (word1, "is NOT an anagram of", word3)
if (sorted(word2) == sorted(word3)):
    print (word2, "is an anagram of", word3)
else:
    print (word2, "is NOT an anagram of", word3)