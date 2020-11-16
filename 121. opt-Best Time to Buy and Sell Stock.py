class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        Min = prices[0]
        ans = 0
        for price in prices:
            Min = min(Min, price)
            ans = max(ans, price-Min)
        return ans
