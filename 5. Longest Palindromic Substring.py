class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        themax = 0
        charList = []
        resultList = []
        for i in range(len(s)):
            charList.append(s[i])
            left = i
            right = i
            while left-1>=0 and right+1<=len(s)-1:
                left-=1
                right+=1
                if s[left] == s[right]:
                    charList.insert(0,s[left])
                    charList.append(s[right])
                else:
                    break
            if len(charList)>themax:
                themax = len(charList)
                resultList = charList
            charList = []

            charList.append(s[i])
            left = i
            right = i
            if i<len(s)-1:
                if s[i+1]==s[i]:
                    charList.append(s[i+1])
                    right+=1
            while left - 1 >= 0 and right + 1 <= len(s) - 1:
                left -= 1
                right += 1
                if s[left] == s[right]:
                    charList.insert(0, s[left])
                    charList.append(s[right])
                else:
                    break
            if len(charList) > themax:
                themax = len(charList)
                resultList = charList
            charList = []


        return ''.join(resultList)

if __name__ == '__main__':
    test = Solution()
    print(test.longestPalindrome('cbbd'))