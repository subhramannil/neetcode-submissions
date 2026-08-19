class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_comb = {}

        for i in strs:
            key = tuple(sorted(i))
            if key not in my_comb:
                my_comb[key] = [i]
            else:
                my_comb[key].append(i)
        return list(my_comb.values())