class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        ans = []
        list = []
        
        for i in range(len(nums)):
            if nums[i] in dict:
                dict[nums[i]] += 1
            else:
                dict[nums[i]] = 1
        for keys, value in dict.items():
            list.append((keys, value))
        new_list = sorted(list, key = lambda e: -e[1])
        for i in range(k):
            ans.append(new_list[i][0])
        return ans
