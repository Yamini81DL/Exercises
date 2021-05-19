# Code your solution here

letter = input().lower()
#print(letter)

lst1 = ['a','e','i','o','u']
if letter in lst1:
    result = "vowel"
else:
    result = "consonant"
    
print(result)
