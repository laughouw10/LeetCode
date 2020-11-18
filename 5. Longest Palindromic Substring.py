import numpy as np
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # reverse = s[::-1]
        sl = len(s)
        table = np.zeros((sl, sl))
        
        max_len = 1
        longest_str = s[0]
        
        for i in range(sl-1):
            if s[i] == s[i+1]:
                max_len = 2
                longest_str = s[i:i+2]
                table[i, i+1] = 2
            table[i, i] = 1
        
        
        k = 2
        while k < sl:
            for i in range(sl-k):
                if s[i] == s[i+k] and table[i+1, i+k-1]:
                    table[i, i+k] = table[i+1, i+k-1]+2
                    if table[i, i+k] > max_len:
                        max_len = table[i, i+k]
                        longest_str = s[i:i+k+1]
            k += 1
        print(table)
        return longest_str
