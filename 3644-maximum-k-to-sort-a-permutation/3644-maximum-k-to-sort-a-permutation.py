class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        ans = -1
        for idx, val in enumerate(nums):
            if val != idx:
                ans &= val
        return ans if ans != -1 else 0
        