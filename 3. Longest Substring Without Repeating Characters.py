class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #方法超时
        # if len(s)>0:
        #     theMax = 1
        #     charList = []
        #     for i in range(len(s)):
        #         theLocal = i
        #         while s[theLocal] not in charList:
        #             charList.append(s[theLocal])
        #             if theLocal<len(s)-1:
        #                 theLocal += 1
        #             else:
        #                 break
        #         if len(charList)>theMax:
        #             theMax = len(charList)
        #         charList = []
        #     return theMax
        # else:
        #     return 0

        # left用于记录合法的左边界位置，last用于记录字符上一次出现的位置
        # 子串中出现重复字符，变更left至上一次s[i]出现位置之后，使得子串合法
        themax = 0
        left = 0
        last = {}
        for i in range(len(s)):
            if s[i] in last and last[s[i]]>=left:
                left = last[s[i]]+1
            last[s[i]] = i
            themax = max(themax,i-left+1)
        return themax



if __name__ == '__main__':
    test = Solution()
    print(test.lengthOfLongestSubstring('pwwkew'))