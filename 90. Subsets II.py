class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(2 ** len(nums)):
            out = []
            num = i
            for j in range(len(nums) - 1, -1, -1):
                if num // (2 ** j) > 0:
                    num -= 2 ** j
                    out.append(nums[j])
            out = sorted(out)
            if out not in ans:
                ans.append(out)
        return ans
