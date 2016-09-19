class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        else:
            result = [[1],[1,1]]
            for i in range(2,numRows):
                listsingle =[1]
                for j in range(1,i):
                    listsingle.append(result[i-1][j]+result[i-1][j-1])
                listsingle.append(1)
                result.append(listsingle)
        return result

test = Solution()
print(test.generate(5))
