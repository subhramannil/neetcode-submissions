class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # l = []
        # l2=[]
        # new = {}
        # new2 = {}
        # for i in s:
        #     l.append(i)
            
        # for i in l:
        #     new[i] = l.count(i)

        # for i in t:
        #     l2.append(i)
            
        # for i in l2:
        #     new2[i] = l2.count(i)
        # if new==new2:
        #     return True
        # else:
        #     return False
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)