class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        ji = [1,3,5,7,9]
        # ou = [2,4,6,8,0]
        while n>1:
            if n%10 in ji:
                n -= 1
                result+=1
                n //= 2
                result += 1
            else:
                n//=2
                result+=1
        return result

if __name__ == '__main__':
    test = Solution()
    print(test.integerReplacement(1234))