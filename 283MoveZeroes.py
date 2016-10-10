class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        flag =0
        while True:
            try:
                nums.remove(0)
                flag+=1
            except:
                break
        for i in range(flag):
            nums.append(0)

        return nums


if __name__ == '__main__':
    test = Solution()
    print(test.moveZeroes([0,0,1,2,3]))
