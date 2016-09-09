class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x>0:
            return self.dealnum(x)
        elif x<0:
            x= abs(x)
            result = 0 - self.dealnum(x)
            return result

    def dealnum(self,x):
        numlist = []
        result = 0
        while x // 10 > 0:
            numlist.append(x % 10)
            x //= 10
        numlist.append(x)
        for i in range(len(numlist)):
            result = result + numlist[i] * (10 ** (len(numlist)-i-1))
        return result

test = Solution()
print(test.reverse(1534236469))