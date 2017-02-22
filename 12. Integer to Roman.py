class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        list_Ge = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        list_shi=["X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        list_bai = ["C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        list_qian = ["M", "MM", "MMM"]
        listzong = [list_Ge,list_shi,list_bai,list_qian]
        resultLIst = []
        thelocal = 0
        stop = False
        while True:
            if num//10 > 0 :
                theflag = num%10
                num //=10
            else:
                theflag = num
                stop = True
            if theflag!=0:
                resultLIst.append(listzong[thelocal][theflag-1])
            else:
                resultLIst.append('')
            thelocal+=1
            if stop:
                break
        resultLIst.reverse()
        return ''.join(resultLIst)

if __name__ == '__main__':
    test =Solution()
    print(test.intToRoman(1001))

