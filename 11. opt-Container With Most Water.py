class Solution:
    def maxArea(self, height: List[int]) -> int:
        s = 0
        d = len(height)-1
        Max_area = 0
        while d > s:
            h = min(height[s], height[d])
            area = (d-s) * h
            Max_area = max(Max_area, area)
            if height[d] < height[s]:
                d -= 1
            else:
                s += 1
        return Max_area
