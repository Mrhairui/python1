class Solution:
    def permute(self, nums):
        def backtrack(first = 0):
            if first == n:
                output.append(nums[:])
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        output = []
        backtrack()
        return output

'''递归的意思就是先处理子问题，然后处理父问题。也就是在流程图中，处理父问题的时候
递归的处理子问题,当然对于排列问题就是要在处理子问题的时候有一个循环遍历的处理，同时
 有交换的处理'''

