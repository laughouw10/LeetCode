class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        result = []
        def helper(nums, result):
            if nums == []:
                result = sorted(result)
                if result not in ans:
                    ans.append(result.copy())
            else:
                num = nums.pop()
                result.append(num)
                helper(nums, result)
                result.pop()
                helper(nums, result)
                nums.append(num)
                
        helper(nums, result)
        return ans
