class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        k = 0
        for i in range(len(nums)):
            k = nums[i]
            nums[i] = "a"
            if k in nums:
                nums[i] = k
            else:
                return k    
