class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        in_list = [0] * N   #be trusted
        out_list = [0] * N  #trust sb.
        for fm, to in trust:
            in_list[to-1] += 1
            out_list[fm-1] += 1
        for i in range(N):
            if in_list[i] == N-1 and out_list[i] == 0:
                return i+1
        return -1
