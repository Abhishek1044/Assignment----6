user_str = str(input("Enter hyphen separated sequence of words : "))

word_list = [n for n in user_str.split("-")] # creating a list of all words after separating them

word_list.sort()

print("Alphabetically sorted hyphen separated list is : ")
print("-".join(word_list))
