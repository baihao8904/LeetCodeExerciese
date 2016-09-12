class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) > len(b):
            maxLen = len(a)
            maxStr = a
            minStr = b
            minLen = len(b)
        else:
            maxLen = len(b)
            minLen = len(a)
            maxStr = b
            minStr = a
        flag = 0
        result = []
        for j in range(minLen,0,-1):
            num =int(maxStr[maxLen-minLen+j-1]) + int(minStr[j-1]) +flag
            print('num',num)
            if num >1:
                result.append(num-2)
                flag = 1
            else:
                result.append(num)
                flag =0
        for i in range(maxLen-minLen,0,-1):
            num2 =  int(maxStr[i-1]) +flag
            if num2 > 1:
                result.append(num2 - 2)
                flag = 1
            else:
                result.append(num2)
                flag = 0
        if flag == 1:
            result.append(1)
        resultStr = ''
        for i in  range(len(result),0,-1):
            resultStr += str(result[i-1])
        return resultStr


test = Solution()
print(test.addBinary('1011','1010'))