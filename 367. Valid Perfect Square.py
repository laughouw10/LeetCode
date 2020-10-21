class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        
        left = 0
        right = num
        n = 0
        while True:
            mid = (left + right) // 2
            if n > 31:
                return False
            elif mid * mid == num:
                return True
            elif mid * mid > num:
                right = mid - 1
                n += 1
            elif mid * mid < num:
                left = mid + 1
                n += 1
