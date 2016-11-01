class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        LeftList = ['{','[','(']
        RightList=['}',']',')']
        strList=[]
        if s[0] in RightList:
            return False
        for i in range(len(s)):
            if s[i] in LeftList:
                strList.append(s[i])
                continue
            if len(strList)>0:
                theFlag = strList.pop()
            else:
                return False
            if LeftList.index(theFlag) == RightList.index(s[i]):
                continue
            else:
                return False
        if len(strList)==0:
            return True
        else:
            return False

if __name__ == '__main__':
    test=Solution()
    print(test.isValid('[{]'))
