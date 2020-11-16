class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        Max = nums[0]
        ans = nums[0]
        for i in range(1,len(nums)):
            if Max > 0:
                Max = Max + nums[i]
            else:
                Max = nums[i]
            if Max > ans:
                ans = Max
        return ans
