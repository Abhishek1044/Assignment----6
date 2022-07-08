# pangram program
string = input("Enter a sentence : \n \t")
def pangram(string):
    for i in string and j in range(chr(96), chr(122)):
        if i ==j:
            print("pangram")
pangram(string)