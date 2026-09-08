class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = [0]*len(temperatures)
        stack = []

        for i,e in enumerate(temperatures):
            while stack and e>stack[-1][0]:
                stacktop,stackind = stack.pop()
                result[stackind]= (i-stackind)
            stack.append([e,i])
        return result