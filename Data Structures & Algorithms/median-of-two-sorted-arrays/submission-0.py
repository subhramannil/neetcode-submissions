class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        c = nums1+nums2
        c.sort()
        n = len(c)
        if n % 2 != 0:
            return float(c[n // 2])
        
        # If length is even, return the average of the two middle elements
        else:
            return (c[(n // 2) - 1] + c[n // 2]) / 2.0