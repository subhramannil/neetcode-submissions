class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        import numpy as np
        l = np.array(matrix).flatten()
        left = 0
        right = len(l)-1
        while left <= right:
            mid = (left+right)//2
            if target==l[mid]:
                return True
            if target<l[mid]:
                right = mid-1
            elif target>l[mid]:
                left = mid+1
        return False