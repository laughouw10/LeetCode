class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        ans = list()
        
        isin = [True, True]
        idx = [0, 0]
        #Suppose we cut intervals as out_0 in_0 out_1 in_1 ... in_n out_n+1
        
        n = len(intervals)
        i = 0
        while i < n and intervals[i][0] <= newInterval[0]: 
            i += 1
        if intervals[i-1][1] < newInterval[0] or i == 0:
            isin[0] = False
            idx[0] = i
        else:
            idx[0] = i-1

        while i < n and intervals[i][0] <= newInterval[1]:
            i += 1
        if intervals[i-1][1] < newInterval[1] or i == 0:
            isin[1] = False
            idx[1] = i
        else:
            idx[1] = i-1
        
        ans.extend(intervals[:idx[0]])
        tmp_list = list()
        if isin[0]:
            tmp_list.append(intervals[idx[0]][0])
        else:
            tmp_list.append(newInterval[0])
        if isin[1]:
            tmp_list.append(intervals[idx[1]][1])
            idx[1] += 1
        else:
            tmp_list.append(newInterval[1])
        ans.append(tmp_list)
        ans.extend(intervals[idx[1]:])
        return ans
