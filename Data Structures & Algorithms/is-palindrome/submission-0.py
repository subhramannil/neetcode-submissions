class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = s.lower()
        n = []
        for i in t:
            if i.isalnum():
                n.append(i)
        a = n[::-1]
        if a==n:
            return True
        else:
            return False