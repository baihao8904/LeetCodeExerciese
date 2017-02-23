class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #S = {-1 2 1 -4}
        # nums.sort()
        # i = 0
        # minFlag = []
        # cha = []
        # while i<len(nums)-1:
        #     left = i+1
        #     right = len(nums)-1
        #     while left<right:
        #         if left+1==right:
        #             minFlag.append(nums[i]+nums[left]+nums[right])
        #             cha.append((nums[i]+nums[left]+nums[right]-target)**2)
        #             break
        #         if nums[i]+nums[left]+nums[right]==target:
        #             return target
        #         elif nums[i]+nums[left]+nums[right] >target:
        #             right-=1
        #         else:
        #             left += 1
        #     i+=1
        # return minFlag[cha.index(min(cha))]
        nums.sort()
        ans = None
        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            while (l < r):
                sum = nums[l] + nums[r] + nums[i]
                if ans is None or abs(sum - target) < abs(ans - target):
                    ans = sum
                if sum <= target:
                    l = l + 1
                else:
                    r = r - 1
        return ans

if __name__ == '__main__':
    test = Solution()
    print(test.threeSumClosest([0,1,1,1],100))

