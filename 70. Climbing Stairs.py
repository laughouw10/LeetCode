class Solution:
    def climbStairs(self, n: int) -> int:
        ans = []
        for i in range(n):
            if i <= 2:
                ans.append(i+1)
            else:
                ans.append(ans[i-2] + ans[i-1])
        return ans[n-1]
