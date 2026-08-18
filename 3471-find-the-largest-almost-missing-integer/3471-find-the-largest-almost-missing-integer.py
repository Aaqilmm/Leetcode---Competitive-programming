class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == n:
            return max(nums)
        if k == 1:
            arr = [i for i in nums if nums.count(i) == 1]
        else:
            arr = [i for i in (nums[0], nums[-1]) if nums.count(i) == 1]
        return max(arr) if arr else -1