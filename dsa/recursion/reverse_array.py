def func(nums,l,r):
    if l>=r:
        return
    nums[l],nums[r]=nums[r],nums[l]
    func(nums,l+1,r-1)
    