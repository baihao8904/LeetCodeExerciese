class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        length = len(digits)
        if digits[length-1] != 9 :
            digits[length-1] = digits[length-1] +1
        else:
            i = length -1
            flag = 0
            while digits[i] == 9 :
                digits[i] = 0
                if i == 0:
                    digits[0] = 0
                    flag = 1
                    break
                else:
                    i -=1
            if flag == 1:
                digits.insert(0,1)
            else:
                digits[i] +=1
        return  digits

test = Solution()
print(test.plusOne([8,9,9,9]))


