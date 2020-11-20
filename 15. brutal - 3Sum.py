class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        lst = sorted(nums)
        
        
        p_lst=[]
        n_lst=[]
        o_lst=[]
        ans=[]
        
        for num in lst:
            if num > 0:
                p_lst.append(num)
            if num < 0:
                n_lst.append(num)
            if num == 0:
                o_lst.append(num)
                
        p_permu_lst = []
        for i in range(len(p_lst)):
            for j in range(i+1,len(p_lst)):
                p_permu_lst.append([p_lst[i],p_lst[j]])
        n_permu_lst = []
        for i in range(len(n_lst)):
            for j in range(i+1,len(n_lst)):
                n_permu_lst.append([n_lst[i],n_lst[j]])
        
        if len(o_lst) >= 3:
            ans.append([0,0,0])
                
        # each select one
        for num in p_lst:
            if -num in n_lst and o_lst:
                if [num,-num,0] not in ans:
                    ans.append([num,-num,0])       
                
        # two neg one pos       
        for num in p_lst:
            for lst in n_permu_lst:
                if num + sum(lst) == 0:
                    if [num, lst[0],lst[1]] not in ans:
                        ans.append([num, lst[0],lst[1]])
            
        # two pos one neg       
        for num in n_lst:
            for lst in p_permu_lst:
                if num + sum(lst) == 0:
                    if [num, lst[0],lst[1]] not in ans:
                        ans.append([num, lst[0],lst[1]])   
        return ans
