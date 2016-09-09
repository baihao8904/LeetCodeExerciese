# -*- coding:utf-8 -*-

nums =[2,7,11,15]
target = 9

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        length = len(nums)
        for i in range(length):
            flag = target - nums[i]
            for num in range(i+1,length):
                if(nums[num]==flag):
                    result.append(i)
                    result.append(num)
                    return result
                else:
                    continue
        return

example = Solution()
print(example.twoSum(nums,target))