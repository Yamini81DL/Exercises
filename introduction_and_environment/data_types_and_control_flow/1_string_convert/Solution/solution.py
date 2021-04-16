# Code your solution here
string = input("Enter a String: ")
#print(type(string))
#data = ""

if string.isupper():
    data = string.lower()
elif string.islower():
    data = string.upper() 
    
print(data)  