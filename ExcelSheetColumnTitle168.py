class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        listcode = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        resultList=[]
        if n<=26:
            return listcode[n-1]
        while n>0:
            if n>=26:
                lastStr = n%26
                if lastStr != 0:
                    n //=26
                else:
                    n = n//26-1
                resultList.append(listcode[lastStr-1])
            else:
                resultList.append(listcode[n-1])
                break
        result = ''.join(resultList[::-1])
        return result


if __name__ == '__main__':
    test = Solution()
    print(test.convertToTitle(53))