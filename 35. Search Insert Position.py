class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i]>=target:
                return i
        return len(nums)

if __name__ == '__main__':
    test = Solution()
    print(test.searchInsert([1],0))