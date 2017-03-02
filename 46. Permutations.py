import itertools


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)==0: return []
        if len(nums)==1: return [nums]
        result = []
        for i in range(len(nums)):
            for j in self.permute(nums[:i]+nums[i+1:]):
                result.append([nums[i]]+j)
        return result

    def permute3(self, num):
        if len(num) == 0: return []
        if len(num) == 1: return [num]
        res = []
        for i in range(len(num)):
            for j in self.permute3(num[:i] + num[i + 1:]):
                res.append([num[i]] + j)
        return res

    def permute2(self, nums):
        return [[n] + p
                for i, n in enumerate(nums)
                for p in self.permute2(nums[:i] + nums[i + 1:])] or [[]]

    def permute5(self,nums):
        return list(map(list,itertools.permutations(nums)))

if __name__ == '__main__':
    test =Solution()
    print(test.permute([1,2,3,4,5]))

