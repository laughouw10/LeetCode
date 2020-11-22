class Solution:
    def search(self, nums: List[int], target: int) -> int:
        dict = {}
        for i in range(len(nums)):
            dict[nums[i]] = i
        return dict[target] if target in nums else -1
