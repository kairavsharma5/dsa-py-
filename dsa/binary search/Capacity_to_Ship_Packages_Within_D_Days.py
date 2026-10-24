class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        n=len(weights)
        def func(weights,capacity):
            day,load=1,0
            for i in range(0,n):
                if (load+weights[i])>capacity:
                    day+=1
                    load=weights[i]
                else:
                    load+=weights[i]
            return day
        low,high=max(weights),sum(weights)
        while(low<=high):
            mid=(low+high)//2
            if(func(weights,mid)<=days):
                high=mid-1
                ans=mid
            else:
                low=mid+1
        return ans
