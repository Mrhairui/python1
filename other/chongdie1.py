from typing import List
class Solution:
    def insert(self, intervals, newInterval):
        output = []
        n = len(intervals)
        if n == 0:
            return [newInterval]
        if newInterval[1] < intervals[0][0] or newInterval[0] > intervals[n-1][1]:
            output = intervals + [newInterval]
            output.sort()
            return output

        for i in range(n):
            if newInterval[1] < intervals[i][0]:
                output.append(newInterval)
                output += intervals[i:n]
                return output
            elif newInterval[0] > intervals[i][1]:
                output.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
                if i == n-1:
                    output.append(newInterval)



        output.sort()

        return output


if __name__ == '__main__':
    solution = Solution()
    intervals = [[1,5]]
    newInterval = [0, 0]
    b =  solution.insert(intervals, newInterval)
    print(b)
