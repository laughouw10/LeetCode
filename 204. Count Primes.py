class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        num_dict = {}
        
        for i in range(n):
            num_dict[i] = -1
            
        num_dict[0] = 0
        num_dict[1] = 0
        
        for i in range(2, n):
            if num_dict[i] == -1:
                num_dict[i] = 1
                for k in range(2 * i, n, i):
                    num_dict[k] = 0
        return sum(num_dict.values())
