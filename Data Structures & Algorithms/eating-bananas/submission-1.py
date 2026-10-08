class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low,high = 1,max(piles)
        res = high
        while low<=high:
            mid = (low+high)//2
            hours = 0
            for i in piles:
                hours+=math.ceil(i/mid)
            if hours<=h:
                high=mid-1
                res = mid
            else:
                low = mid+1
        return res