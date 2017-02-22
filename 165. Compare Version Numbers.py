class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        while version1[0]=='0' and len(version1)>1:
            version1 = version1[1:]
        while version2[0]=='0' and len(version2)>1:
            version2 = version2[1:]

        print(version1,version2)
        version1List = version1.split('.')
        version2List = version2.split('.')
        for i in range(min(len(version1List),len(version2List))):
            if version1List[i]>version2List[i]:
                return 1
            elif version1List[i]<version2List[i]:
                return -1

        if len(version1List)>len(version2List):
            return 1
        elif len(version1List)==len(version2List):
            return 0
        else:
            return -1

if __name__ == '__main__':
    test = Solution()
    print(test.compareVersion('1','01'))