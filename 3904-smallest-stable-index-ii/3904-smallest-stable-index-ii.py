class Solution:
    def firstStableIndex(self, nums, k):
        n = len(nums)

        ansIdx = 0
        globalMax = float('-inf')
        ansMax = float('-inf')

        for i in range(n):
            globalMax = max(globalMax, nums[i])
            if i == ansIdx:
                ansMax = max(ansMax, nums[i])
            if nums[i] < ansMax - k:
                ansIdx = i + 1
                ansMax = globalMax

        return ansIdx if ansIdx < n else -1