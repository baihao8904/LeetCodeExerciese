class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2:
            return n
        result=[1,2]
        for i in range(n-2):
            result.append(result[-2]+result[-1])
        return result[-1]
if __name__ == '__main__':
    test = Solution()
    print(test.climbStairs(5))
