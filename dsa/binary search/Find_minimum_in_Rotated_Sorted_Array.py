def findMin( nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mini=float("inf")
        n=len(nums)
        low=0
        high=n-1
        while(low<=high):
            mid=(low+high)//2
            if(nums[mid]<=nums[high]):
                mini=min(mini,nums[mid])
                high=mid-1
            else:
                mini=min(mini,nums[low])
                low=mid+1
        return mini

nums=[3,4,5,1,2]
b=findMin(nums)
print(b)