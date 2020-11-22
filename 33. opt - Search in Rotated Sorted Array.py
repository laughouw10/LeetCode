class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target in nums:
            if target < nums[0]:
                nums[::-1]
            ans = 0
            while True:
                if nums[ans] == target:
                    return ans
                ans += 1
        return -1
