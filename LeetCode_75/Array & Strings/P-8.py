'''
Increasing Triplet Subsequence

Given an integer array nums, return true if there exists a triple of 
indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. 
If no such indices exists, return false.
'''


nums = input("Enter an array of numbers: ").split()

for i in range(len(nums)):
    nums[i] = int(nums[i])

length = len(nums)
found = False

for i in range(length):
    for j in range(i + 1, length):
        for k in range(j + 1, length):
            if nums[i] < nums[j] and nums[j] < nums[k]:
                found = True
                break
        if found:
            break
    if found:
        break

if found:
    print(True)
else:
    print(False)


'''
class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        
        first = float('inf')
        second = float('inf')

        for i in range(len(nums)):
            if nums[i] <= first:
                first = nums[i]
            elif nums[i] <= second:
                second = nums[i]
            else:
                return True   # found third element

        return False
'''