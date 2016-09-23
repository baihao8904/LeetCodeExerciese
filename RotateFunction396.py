class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        #超时
        # resultList  = []
        # for j in range(len(A)):
        #     result=0
        #     for i in range(len(A)):
        #         result += i*A[i]
        #     resultList.append(result)
        #     lastone = A.pop()
        #     A.insert(0,lastone)
        # if len(resultList)==0:
        #     return 0
        # maxone= max(resultList)
        # return maxone

if __name__ == '__main__':
    test =Solution()
    print(test.maxRotateFunction([-2147483648,-2147483648]))