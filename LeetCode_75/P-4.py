'''
Can Place Flowers

You have a long flowerbed in which some of the plots are planted, 
and some are not. However, flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's,
where 0 means empty and 1 means not empty, and an integer n,
return true if n new flowers can be planted in the flowerbed without
violating the no-adjacent-flowers rule and false otherwise.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
'''
print("Empty flower beds are represented by 0's")
print("Non-Empty flower beds are represented by 1's")

flower_bed = []
length = int(input("Enter the length of flower_bed:-"))
for i in range(length):
    value = int(input(f"Status of place {i}:-"))
    flower_bed.append(value)
print(flower_bed)
n = int(input("Enter the flowers to be planted:-"))

count = 0

for i in range(length):
    if flower_bed[i] == 0:
        left = (i == 0) or (flower_bed[i-1] == 0)
        right = (i == length -1 ) or  (flower_bed[i+1] == 0)

        if left and right:
            flower_bed[i] = 1
            count +=1

if count >= n:
    print("True")
else:
    print("False") 

'''
from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        length = len(flowerbed)

        for i in range(length):
            if flowerbed[i] == 0:
                left = (i == 0) or (flowerbed[i - 1] == 0)
                right = (i == length - 1) or (flowerbed[i + 1] == 0)

                if left and right:
                    flowerbed[i] = 1
                    count += 1
                    if count >= n:
                        return True

        return count >= n
'''