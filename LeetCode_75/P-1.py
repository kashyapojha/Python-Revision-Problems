'''
You are given two strings word1 and word2.
Merge the strings by adding letters in alternating order, starting with word1. 
If a string is longer than the other, append the additional letters onto the end of the merged string.
Return the merged string.
'''


word1 = input("Enter the word1:-")
word2 = input("Enter the word2:-")

i = 0
j = 0
result = ""
while i < len(word1) and j < len(word2):
    result += word1[i]
    result += word2[j]
    i += 1
    j += 1

result += word1[i:]  
result += word2[j:]

print("Merged string is", result)


