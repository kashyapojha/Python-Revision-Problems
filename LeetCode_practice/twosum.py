nums=[]
length=int(input("Enter the length of nums array:-"))
for i in range(length):
    element = int(input(f"Enter element{i+1}: "))
    nums.append(element)
print("Array is", nums)

target = int(input("Enter the target number:-"))

indexes = []

for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i] + nums[j] == target:
            indexes.append((i,j))
print("Indexes are", indexes) 



