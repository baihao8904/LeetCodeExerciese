class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums)<1:
            return 0

        take = 0
        nontake =0
        maxProfile = 0

        for house in nums:
            take = nontake + house
            nontake = maxProfile
            maxProfile = max(nontake,take)

        return maxProfile