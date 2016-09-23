class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        resultset=set()
        while True:
            numlist = []
            while n >= 1:
               numlist.append(n%10)
               n //= 10
            length = len(numlist)
            for i in range(length):
                n += numlist[i] **2
            if n in resultset:
                return False
            else:
                resultset.add(n)
            if n==1:
                return True

if __name__ == '__main__':
    test = Solution()
    print(test.isHappy(3))
