class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        while n:
            ans += n&1
            n>>=1
        return ans

        # ans = 0
        # while n:
        #     n &= n - 1
        #     ans += 1
        # return ans
if __name__ == '__main__':
    test=Solution()
    print(test.hammingWeight(5))