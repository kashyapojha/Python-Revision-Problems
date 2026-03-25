'''
You are given two strings word1 and word2.
Merge the strings by adding letters in alternating order, starting with word1. 
If a string is longer than the other, append the additional letters onto the end of the merged string.
Return the merged string.
'''
word1 = str(input("Enter the word-1:-"))
word2 = str(input("Enter the word-2:-"))
i = 0  
j = 0
result = ""
while i < len(word1) and i < len(word2):
    result += word1[i]
    result += word2[i]
    i += 1
    j += 1

result += word1[i:]
result += word2[j:]

print("Merged string is " , result)



    