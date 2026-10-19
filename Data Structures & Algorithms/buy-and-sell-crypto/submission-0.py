class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = []
        if all(prices[i] >= prices[i+1] for i in range(len(prices)-1)):
            return 0
        else:
            for i in range(0,len(prices)):
                for j in range(len(prices)-1,i,-1):
                    res.append(prices[j]-prices[i])
            return max(res)