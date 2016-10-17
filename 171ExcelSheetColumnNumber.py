class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        for i in range(len(s)-1,-1,-1):
            stepnum = (ord(s[i])-64)*(26**(len(s)-1-i))
            num+=stepnum
        return num


if __name__ == '__main__':
    test = Solution()
    print(test.titleToNumber('AB'))