class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
#数组给出了每一天的股价 求出何时买卖操作可以获得最高的利润
        #超时
        # maxprice = 0
        # minprice = 0
        # profix = 0
        # for i in range(len(prices)-1,-1,-1):
        #     if prices[i] > maxprice:
        #         maxprice = prices[i]
        #         minprice = maxprice
        #     for j in range(i-1,-1,-1):
        #         if prices[j]<minprice:
        #             minprice = prices[j]
        #     if maxprice - minprice >profix:
        #         print('max',maxprice,'min',minprice)
        #         profix = maxprice - minprice
        # return profix
        if len(prices)==0:
            return 0
        maxprice = prices[-1]
        profix = 0
        for i in range(len(prices)-1,-1,-1):
            maxprice = max(maxprice,prices[i])
            profix = max(profix,maxprice-prices[i])
        return profix




if __name__ == '__main__':
    test = Solution()
    print(test.maxProfit([7, 1, 5, 3, 6, 4]))
    #test2 [7, 6, 4, 3, 1]