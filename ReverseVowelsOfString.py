class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        #超时
        # originList = list(s)
        # vowelList = []
        # for item in originList:
        #     if item in ['a','e','i','o','u','A','E','I','O','U']:
        #         vowelList.append(item)
        # j=-1
        # for i in range(len(originList)):
        #     if originList[i] in ['a','e','i','o','u','A','E','I','O','U']:
        #         originList[i] = vowelList[j]
        #         j-=1
        # result =''
        # for item in originList:
        #     result += item
        # return  result

        strlist = list(s)
        start = 0
        end = len(strlist)-1
        vowels =['a','e','i','o','u']
        while start<end:
            print(start,end)
            while start<end and strlist[start].lower() not in vowels:
                start +=1
            while start<end and strlist[end].lower() not in vowels:
                end -=1
            if strlist[start] != strlist[end]:
                strlist[start],strlist[end] = strlist[end],strlist[start]
            start+=1
            end-=1
        result=''.join(strlist)
        return result




test =Solution()
print(test.reverseVowels('hello'))


