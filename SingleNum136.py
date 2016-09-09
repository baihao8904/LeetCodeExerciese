class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sortNums = sorted(nums)
        print(sortNums)
        listnum = sorted(list(set(nums)))
        print(listnum)
        for i in range(len(listnum)):
            try:
                sortNums.remove(listnum[i])
                sortNums.remove(listnum[i])
            except:
                return listnum[i]

        return sortNums[0]

test = Solution()
print(test.singleNumber([1,1,3,3,4,5,5]))





