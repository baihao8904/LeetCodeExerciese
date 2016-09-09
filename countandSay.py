class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        nextnum =1
        while n==1:
            nextnum = self.findnextnum(nextnum)
            n-=1
        return str(nextnum)

    def findnextnum(self,x):
        strnum = str(x)
        print(strnum)
        data = []
        datanum = []
        while len(strnum)>0:
            flag = 1
            dataindex = strnum[0]
            data.append(dataindex)
            for i in range(len(strnum)-1):
                if strnum[i+1] == dataindex:
                    flag+=1
                else:
                    break
            datanum.append(str(flag))
            strnum = strnum[flag:]
        nextnum =''
        for i in range(len(data)):
            nextnum = nextnum + datanum[i]+data[i]
        nextnum=int(nextnum)
        return nextnum

text =Solution()
print(text.countAndSay(5))

