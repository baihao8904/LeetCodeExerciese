# -*- coding:utf-8 -*-

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        flag = 0
        for i in range(len(nums)-1):
            if nums[i-flag] == nums[i+1-flag]:
                del nums[i-flag]
                print(nums)
                flag+=1
        return len(nums)

test = Solution()
print(test.removeDuplicates([1,1,2,3,4,5,6,6]))