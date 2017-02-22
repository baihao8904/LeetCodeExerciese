class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<3 and n!=1:
            return False
        elif n==1:
            return True
        while n%3==0 and n>=3:
            n /= 3
        if n>1:
            return False
        return True

if __name__ == '__main__':
    print()