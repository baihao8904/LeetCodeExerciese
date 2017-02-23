class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #时间复杂度n立方的做法
        # uniquenum = list(set(nums))
        # resultList =[]
        # for num in uniquenum:
        #     nums.remove(num)
        #     for L in range(0,len(nums)-1):
        #         for R in range(L+1,len(nums)):
        #             if nums[L]+nums[R] == -num :
        #                 alist = [nums[L],nums[R],num]
        #                 alist.sort()
        #                 if alist not in resultList:
        #                     resultList.append(alist)
        #                 else:
        #                     continue
        #             else:
        #                 continue
        # return resultList
        nums.sort()
        resultList = []
        for i in range(0,len(nums)-2):
            if i>0:
                if nums[i] == nums[i-1]:
                    continue
            target = nums[i] * -1
            left = i+1
            right = len(nums)-1
            while left<right:
                if nums[left]+nums[right] == target:
                    resultList.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left<right and nums[left-1] == nums[left]:
                        left+=1
                    while left<right and nums[right + 1] == nums[right]:
                        right -= 1
                elif target>nums[left]+nums[right]:
                    left+=1
                else :
                    right-=1
        return resultList



if __name__ == '__main__':
    test = Solution()
    S = [-2,0,1,1,2]
    print(test.threeSum(S))