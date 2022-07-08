string = input("Enter a word , phrase or sentence : \n")
string = string.lower()
newstring = ""
for i in string:
    newstring = i + newstring
    
if newstring == string :
    print(f"{string} is a palindrome ")
else:
    print(f"{string} is not palindrome")