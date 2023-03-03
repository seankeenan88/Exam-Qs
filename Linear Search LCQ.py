names = ["John", "Mary", "Zoe","Alex","Séamas"]

name = input("Enter lookup name: ")

found = False
index = 0

while (not found) and (index != len(names)):
    if name == names[index]:
        found = True
    else:
        index = index + 1
        
print("Result:", index)