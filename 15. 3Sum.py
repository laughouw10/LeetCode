class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums = sorted(nums)
        dup = collections.defaultdict(bool)
        
        j = 0
        while j<len(nums) and nums[j] == 0:
            j += 1
            
        if j >= 3:
            return [[0, 0, 0]]
        elif j:
            return []
        
        prev = nums[0]
        
        o_num = 0
        p_list = []
        n_list = [prev]
        
        for i in range(1, len(nums)):
            if nums[i] == 0:
                o_num += 1
                continue
                
            if nums[i] == prev:
                dup[prev] = True
                continue   
            prev = nums[i]
            
            dup[prev] = False
            if nums[i] < 0:
                n_list.append(nums[i])
            elif nums[i] > 0:
                p_list.append(nums[i])
        

        ans = []

        
        for i1, n in enumerate(n_list):
            for i2, p in enumerate(p_list):
                tmp = n+p
                if tmp == 0 and o_num:
                    ans.append([n, 0, p])
                elif -tmp == n or -tmp == p:
                    if dup[-tmp]:
                        ans.append([n, -tmp, p])
                elif -tmp in dup:
                    if tmp > 0 and -tmp > n:
                        ans.append([n, -tmp, p])
                    if tmp < 0 and -tmp > p:
                        ans.append([n, p, -tmp])
                    
        if o_num >= 3:
            ans.append([0, 0, 0])
        return ans
