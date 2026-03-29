'''
Reverse Vowels of a String

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 Example 1:
Input: s = "IceCreAm"
Output: "AceCreIm"

Explanation:
The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:
Input: s = "leetcode"
Output: "leotcede"
'''
string = input("Enter the string:-")
vowels = "AEIOUaeiou"
found = False 
vowels_in_string = []
other_char = []
rev_vowels = []
final_string = []

for i in string:
        if i in vowels:
            found = True
            vowels_in_string.append(i)
        else:
             other_char.append(i)
print("vowels in string are:", vowels_in_string)
vowels_in_string.reverse()
rev_vowels = vowels_in_string
print("Reversed vowels", rev_vowels)

merged_string = []
j = 0 
for i in string:
     if i in vowels:
          merged_string.append(rev_vowels[j])
          j += 1
     else:
          merged_string.append(i)

final_string = "".join(merged_string)
print("Final string:", final_string)



if not found:
    print("There are no vowels")

'''
class Solution:
    def reverseVowels(self, s: str) -> str:
        
        vowels = "AEIOUaeiou"
        found = False 
        vowels_in_string = []
        rev_vowels = []
        final_string = []

    
        for i in s:
            if i in vowels:
                found = True
                vowels_in_string.append(i)

        
        vowels_in_string.reverse()
        rev_vowels = vowels_in_string

        
        merged_string = []
        j = 0 
        
        for i in s:
            if i in vowels:
                merged_string.append(rev_vowels[j])
                j += 1
            else:
                merged_string.append(i)

        final_string = "".join(merged_string)

        return final_string
'''