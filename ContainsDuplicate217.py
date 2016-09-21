class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        newList = list(set(nums))
        if len(newList)<len(nums):
            return True
        else:
            return False