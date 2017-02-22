class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        #cmp函数中，返回正数表示大于 返回负数表示小于  0 表示等于
        #两字符串相加返回的字符串相比较
        nums = sorted(nums, cmp=lambda x, y: 1 if str(x) + str(y) < str(y) + str(x) else -1)
        largest = ''.join([str(x) for x in nums])
        i, length = 0, len(largest)
        while i + 1 < length:
            if largest[i] != '0':
                break
            i += 1
        return largest[i:]

if __name__ == '__main__':
    test = Solution()
    print(1)
    print('9'>'1')