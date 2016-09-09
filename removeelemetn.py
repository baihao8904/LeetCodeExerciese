class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = len(nums)
        print(length)
        while length > 0:
            print(1)
            if nums[length-1] == val:
                del nums[length-1]
            length-=1
        print(nums)
        return len(nums)

test = Solution()
nums=[3,3,2,2]
val=3
print(test.removeElement(nums,val))