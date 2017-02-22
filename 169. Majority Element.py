class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        aDict = {}
        for i in nums:
            if aDict.get(i) is not None:
                aDict[i] +=1
            else:
                aDict[i] = 1

        for i in aDict.keys():
            if aDict[i]>(len(nums)/2):
                return i

if __name__ == '__main__':
    test = Solution()
    print(test.majorityElement([1,2,1,2,1,2,2]))
