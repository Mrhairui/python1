class Solution:
    def merge(self, intervals):
        output = []
        n = len(intervals)
        intervals.sort()
        if n == 1:
            return intervals
        for i in range(n-1):
            if intervals[i][1] < intervals[i+1][0]:
                output.append(intervals[i])
            else:
                tmp = [intervals[i][0], max(intervals[i+1][1], intervals[i][1])]
                intervals[i+1] = tmp
            if i == n - 2:
                output.append(intervals[i+1])
        return output


if __name__ == '__main__':
    solution = Solution()
    nums = [[1,4],[4,5]]
    b =  solution.merge(nums)
    print(b)