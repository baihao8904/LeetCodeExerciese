class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        listStr = s.strip().split(' ')
        print(listStr)
        if len(listStr)>0:
            return len(listStr[-1])
        else:
            return 0

if __name__ == '__main__':
    test =Solution()
    print(test.lengthOfLastWord(" "))