class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stackList = []
        self.minstack = []


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stackList.append(x)
        if len(self.minstack)>0:
            if x <= self.minstack[-1]:
                self.minstack.append(x)
        else:
            self.minstack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self.stackList[-1] == self.minstack[-1]:
            self.minstack.pop()
        return self.stackList.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stackList[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minstack[-1]


        # Your MinStack object will be instantiated and called as such:
        # obj = MinStack()
        # obj.push(x)
        # obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.getMin()
if __name__ == '__main__':
    test = MinStack()
    test.push(1)
    test.push(2)
    test.push(-3)
    test.push(5)
    print(test.stackList)
    print(test.top(),test.pop())
    print(test.getMin())
    print(test.stackList)