class Solution:
    def maxArea(self, height: List[int]) -> int:
        max = 0
        for idx,num in enumerate(height):
            for i in range(idx, len(height)):
                if min(height[i], num) * (i - idx) > max:
                    max = min(height[i], num) * (i - idx)
        return max
