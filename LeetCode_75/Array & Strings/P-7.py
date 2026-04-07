# Product of Array Except Self

'''
Given an integer array nums, return an array answer such that 
answer[i] is equal to the product of all the elements of nums 
except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 
32-bit integer.
You must write an algorithm that runs in O(n) time and without using
the division operation.
'''
nums = list(map(int, input("Enter numbers (space separated): ").split()))

n = len(nums)
answer = [1] * n

prefix = 1
for i in range(n):
    answer[i] = prefix 
    prefix *= nums[i]

suffix = 1
for i in range(n - 1, -1 , -1):
    answer[i] *= suffix
    suffix *= nums[i]
print("Output:", answer)

'''
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        # Prefix
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        # Suffix
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer
        '''