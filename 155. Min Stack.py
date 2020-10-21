class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.list = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        self.list = self.list + [x]
        

    def pop(self):
        """
        :rtype: None
        """
        self.stack = self.stack[:-1]
        self.list = self.list[:-1]
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        n = 10000000000000
        for i in range(len(self.list)):
            if n > self.list[i]:
                n = self.list[i]
        return n


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
