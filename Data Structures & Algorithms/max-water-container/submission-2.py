class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start,end = 0, len(heights)-1
        count = []
        while start<end:
            count.append(abs((start-end)*min(heights[start],heights[end])))
            if heights[start]<heights[end]:
                start+=1
            else:
                end-=1
        return max(count)