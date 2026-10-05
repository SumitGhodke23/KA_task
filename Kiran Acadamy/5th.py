word1 = input("Enter 1st word: ")
word2 = input("Enter 2nd word: ")

if sorted(word1.lower()) == sorted(word2.lower()):
    print("The words are Anagrams")
else:
    print("The words are not Anagrams")
