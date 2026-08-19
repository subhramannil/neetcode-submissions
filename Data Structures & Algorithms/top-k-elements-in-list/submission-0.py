class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            if num not in count:
                count[num] = 0
                count[num] += 1
            elif num in count:
                count[num] += 1
        
        sorted_dict = {k: v for k, v in sorted(count.items(), key=lambda item: item[1], reverse = True)}

        d = list(sorted_dict.keys())[:k]
        return d