class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        lengthS = len(s)
        lengthT = len(t)
        listjudge =[]
        if lengthT==lengthS:
            for i in s:
                listjudge.append(i)
            totaljudge = set(listjudge)
            for i in range(len(totaljudge)):
                if s.count(totaljudge[i])==t.count(totaljudge[i]):
                    pass
                else:
                    return False
            return True
        else:
            return False

test = Solution()
s="12"
t="1"
print(test.isAnagram(s,t))