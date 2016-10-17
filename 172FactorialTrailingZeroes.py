class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        theNum = 5
        numsofFive = 0
        while theNum<=n:
            numsofFive += n//theNum
            theNum *=5
        return numsofFive

if __name__ == '__main__':
    test =Solution()
    print(test.trailingZeroes(5))