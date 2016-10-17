class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ans = 0
        while n :
            lastnum = n&1
            n >>=1
            ans = ans|lastnum
            ans<<=1
        return ans

if __name__ == '__main__':
    test = Solution()
    print(test.reverseBits(1))