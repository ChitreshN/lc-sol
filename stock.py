class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 0
        cur = 0
        res = 0
        for k in range(len(prices)):
            if prices[k] < prices[i]:
                i = k
                j = k
            if prices[j] < prices[k]:
                j = k
            cur = prices[j] - prices[i]
            res = max(cur,res)
        return res
