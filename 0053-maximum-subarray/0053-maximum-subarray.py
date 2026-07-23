class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cs = -1000000
        ms = -1000000
        for i in range(len(nums)):
            cs = max(nums[i], cs + nums[i])
            ms = max(ms, cs)
        return ms