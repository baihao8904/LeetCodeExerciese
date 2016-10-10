# 1~9: {"I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"};
#
# 10~90: {"X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"};
#
# 100~900: {"C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"};
#
# 1000~3000: {"M", "MM", "MMM"}.

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        data ={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        result = 0
        for i in range(1,len(s)+1):
            while i<len(s):
                if data[s[i-1]] < data[s[i]]:
                    result -= data[s[i-1]]*2
                break
            result += data[s[i-1]]

        return result

if __name__ == '__main__':
    test = Solution()
    print(test.romanToInt('DCXXI'))