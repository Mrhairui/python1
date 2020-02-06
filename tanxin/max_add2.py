class Solution:
    def maxSubArray(self, nums):
        n = len(nums)
        if n == 1:
            return nums[0]
        else:
            max_left = self.maxSubArray(nums[0:len(nums)//2])
            max_right = self.maxSubArray(nums[len(nums)//2:len(nums)])
        max_l = nums[len(nums)//2-1]
        tmp = 0
        for i in range(len(nums)//2-1, -1, -1):
            tmp += nums[i]
            max_r = max(tmp, max_l)
        max_r = nums[len(nums)//2]
        tmp = 0
        for i in range(len(nums)//2, len(nums)):
            tmp += nums[i]
            max_r = max(tmp, max_r)
        return max(max_right, max_left, max_l + max_r)