class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i,j in enumerate(nums):
            if i > 0 and j == nums[i - 1]:
                continue
            
            left = i+1
            right = len(nums)-1
            while left<right:
                add = nums[left]+nums[right]+j

                if add == 0:
                    result.append([j,nums[left],nums[right]])
                    left +=1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                elif add<0:
                    left = left + 1

                elif add>0:
                    right = right - 1 

        return result