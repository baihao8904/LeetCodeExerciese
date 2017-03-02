class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
#S = [1, 0, -1, 0, -2, 2], and target = 0.
        nums.sort()
        result = []
        for i in range(0,len(nums)-3):
            outright = len(nums) - 1
            if nums[i]+nums[i+1]+nums[i+2]+nums[i+3]>target:
                break
            if i and nums[i]==nums[i-1]:
                continue
            while outright>i+2:
                thetarget = target-nums[i]-nums[outright]
                inleft = i+1
                inright = outright-1
                while inleft<inright:
                    if nums[inleft]+nums[inright]==thetarget:
                        result.append([nums[i],nums[inleft],nums[inright],nums[outright]])
                        inleft+=1
                        while inleft<inright and nums[inleft-1]==nums[inleft]:
                            inleft+=1
                        inright-=1
                        while inleft<inright and nums[inright+1]==nums[inright]:
                            inright-=1
                    elif nums[inleft]+nums[inright]>thetarget:
                        inright-=1
                    elif nums[inleft]+nums[inright]<thetarget:
                        inleft+=1
                outright-=1
                while nums[outright+1]==nums[outright] and outright>i+2:
                    outright-=1
        return (result)

if __name__ == '__main__':
    test = Solution()
    print(test.fourSum([0,0,0,0],0))
