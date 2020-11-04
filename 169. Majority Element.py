class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = defaultdict(lambda: 0)
        for i in range(len(nums)):
            dict[nums[i]] += 1
        list = sorted(dict.items(), key = lambda kv: kv[1])
        return list[-1][0]
