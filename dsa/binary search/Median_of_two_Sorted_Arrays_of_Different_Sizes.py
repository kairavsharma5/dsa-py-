class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        a, b = nums1, nums2
        n1, n2 = len(a), len(b)

        # always binary search on the smaller array
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)

        low, high = 0, n1
        left = (n1 + n2 + 1) // 2      # size of the combined left half
        n = n1 + n2

        while low <= high:
            mid1 = (low + high) // 2   # elements taken from a for the left half
            mid2 = left - mid1         # elements taken from b for the left half

            l1 = l2 = float('-inf')
            r1 = r2 = float('inf')

            if mid1 < n1:
                r1 = a[mid1]
            if mid2 < n2:
                r2 = b[mid2]
            if mid1 - 1 >= 0:
                l1 = a[mid1 - 1]
            if mid2 - 1 >= 0:
                l2 = b[mid2 - 1]

            if l1 <= r2 and l2 <= r1:          # valid split
                if n % 2 == 1:
                    return float(max(l1, l2))
                return (max(l1, l2) + min(r1, r2)) / 2.0

            elif l1 > r2:                      # took too many from a
                high = mid1 - 1
            else:                              # took too few from a
                low = mid1 + 1

        return 0.0
        