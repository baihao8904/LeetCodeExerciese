class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        result = num
        stepresult = 0
        while True:
            while result>=10:
                stepresult += result%10
                result //=10
            stepresult += result
            if stepresult>=10:
                result = stepresult
                stepresult =0
            else:
                break
        return stepresult


if __name__ == '__main__':
    test = Solution()
    print(test.addDigits(38))