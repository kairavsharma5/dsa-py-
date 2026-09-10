nums = [1, 3, 2, 4, 2, 323, 91, 34, 4, 0]
n = len(nums)
for i in range(n-1, 0, -1):        
    for j in range(0, i):          
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
print(nums)
# Output: [0, 1, 2, 2, 3, 4, 4, 34, 91, 323]  ✓ correct
# tc = O(n^2)