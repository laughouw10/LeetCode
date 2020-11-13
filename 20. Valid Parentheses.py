class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        
        lst = []
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                lst.append(s[i])
            else:
                if len(lst) == 0:
                    return False
                ch = lst.pop()
                if ch == "(" and s[i] != ")":
                    return False
                if ch == "[" and s[i] != "]":
                    return False
                if ch == "{" and s[i] != "}":
                    return False
        return len(lst) == 0
                
