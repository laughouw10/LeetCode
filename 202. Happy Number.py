k = 0
class Solution(object):
    def isHappy(self, n):
        global k
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            k = 0
            return True
        if k > 100:
            k = 0
            return False
        else:
            k += 1
            list = []
            while n != n % 10 :
                list.append(n % 10)
                n = n//10
            list.append(n)
            m = 0
            for i in range(len(list)):
                m += list[i]**2
            return self.isHappy(m)
