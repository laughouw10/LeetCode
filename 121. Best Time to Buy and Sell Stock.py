class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        lst = []
        for i in range(len(prices)):
            lst.append(max(prices[i:]) - prices[i])
        return max(lst)
