class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        else:
            result = [1,1]
            for i in range(1,rowIndex):
                newResult=[1,1]
                for _l in range(1,len(result)):
                    print(_l)
                    newResult.insert(_l,result[_l]+result[_l-1])
                result = newResult
            return result

test =Solution()
print(test.getRow(4))