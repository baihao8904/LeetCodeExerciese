class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ListS = list(s)
        ListT = list(t)
        ansList=[]
        for i in range(len(ListT)-1,-1,-1):
            if ListT[i] in ListS:
                ListT.pop()
            else:
                ansList.append(ListT.pop())
        # ansList = ansList.reverse()
        ansList.reverse()
        result = ''.join(ansList)
        return result

if __name__ == '__main__':
    test =Solution()
    print(test.findTheDifference('abcd','abcdef'))