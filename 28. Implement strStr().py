class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
        if len(needle) > len(haystack):
            return -1

        lenSource = len(haystack)
        lenTarget = len(needle)
        for i in range(lenSource-lenTarget+1):
            j =0
            while (j<lenTarget):
                if needle[j] != haystack[i+j]:
                    break
                j+=1
            if j==lenTarget:
                return i
        return -1



if __name__ == '__main__':
    test =Solution()
    print(test.strStr("mississippi","issipi"))