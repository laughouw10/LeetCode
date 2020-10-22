class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def helper(curr_lst, arr):
            if len(arr) == 0:
                result.append(curr_lst)
            else:
                for i in range(len(arr)):
                    helper(curr_lst + [arr[i]], arr[:i] + arr[i+1:])   
        helper([],nums)
        return result
