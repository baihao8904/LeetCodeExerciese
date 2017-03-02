class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits)==0:
            return []
        dict = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            "8":['t','u','v'],
            '9':['w','x','y','z']
        }
        readyList = []
        for i in range(len(digits)):
            readyList.append(dict[digits[i]])
        result = [readyList[0]]
        for i in range(1,len(readyList)):
            thelist = []
            for item in result[-1]:
                for initem in readyList[i]:
                    thelist.append(item+initem)
            result.append(thelist)
        return result[-1]

if __name__ == '__main__':
    test = Solution()
    print(test.letterCombinations('223'))