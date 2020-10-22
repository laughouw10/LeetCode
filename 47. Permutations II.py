class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        list = []
        def perm(nums, list):
            if len(nums) == 0:
                if list not in ans:
                    ans.append(list)
            else:
                for i in range(len(nums)):
                    # list += [nums[i]] 不能直接改變list
                    perm(nums[:i]+nums[i+1:], list + [nums[i]])
        perm(nums, list)
        return ans
