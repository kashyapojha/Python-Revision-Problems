# Move Zeroes 

'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]
 '''
nums = list(map(int, input("Enter elements separated by space: ").split()))
length = len(nums)
j = 0
for i in range(length):
    if nums[i] != 0:
        nums[j] = nums[i]
        j += 1
for i in range(j, length):
    nums[i] = 0
print("Array after shifting:", nums)

'''
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0  

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
'''