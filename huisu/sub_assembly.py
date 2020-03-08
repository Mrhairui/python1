class Solution:
    def subsetsWithDup(self, nums):
        if not nums:
            return []
        n = len(nums)
        res = []
        nums.sort()
        def helper2(idx, n, tmp_list):
            res.append(tmp_list)
            for i in range(idx, n):
                if i > idx and nums[i] == nums[i-1]:
                    continue
                helper2(i+1, n ,tmp_list + [nums[i]])


        helper2(0, n, [])
        return res





