class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        strx = str(x)
        for i in range(len(strx)//2):
            if strx[i] == strx[len(strx)-1-i]:
                pass
            else:
                return False

        return True

if __name__ == '__main__':
    test = Solution()
    print(test.isPalindrome(1211))