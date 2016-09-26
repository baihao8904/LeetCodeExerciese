# -*- coding:utf-8 -*-
#判断是否是2的次方数
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        ouList = [0,2,4,6,8]
        while n>=1:
            if n==1:
                return True
            lastNum = n%10
            if lastNum not in ouList:
                return False
            if n != 1:
                n /=2
        return False

if __name__ == '__main__':
    test = Solution()
    print(test.isPowerOfTwo(7))