class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cand = []

        for i,v in enumerate(nums):
            new_target = target - v
            for j,k in enumerate(nums):
                if i!=j:
                    if new_target==k:
                        cand.append(i)
                        cand.append(j)
                        
            new_target = target
        new_cand1 = set(cand)
        new_cand2 = list(new_cand1)
        return new_cand2