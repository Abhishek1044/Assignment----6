# pangram program
alphabets = "abcdefghijklmnopqrstuvwxyz"

def ispangram(userstr):
    for x in alphabets:
        if x not in userstr.lower():
            return False
    return True

input_str = str(input("Enter string to be checked if pangram or not : "))

if(ispangram(input_str)==True):
    print("Yes, it is a pangram.")
else:
    print("No, it is not a pangram.")
