# -*- coding:utf-8 -*-
#Ascii操作 ord chr

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool

                """
        aList = []
        for i in range(len(s)):
            if 97<=ord(s[i])<=122 :
                aList.append(s[i].upper())
            elif 65<=ord(s[i])<=90:
                aList.append(s[i])
            elif 48<=ord(s[i])<=57:
                aList.append(s[i])
        for i in range(len(aList)//2):
            if aList[i] == aList[-(i+1)]:
                continue
            else:
                return False
        return True

if __name__ == '__main__':
    test = Solution()
    print(test.isPalindrome("a."))
    print(ord('0'))