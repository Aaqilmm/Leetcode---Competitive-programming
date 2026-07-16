class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n= len(nums)
        mx= []
        Max= -inf
        for x in nums:
            Max = max(Max, x)
            mx.append(Max)
        Gcd = [gcd(x, y) for x, y in zip(nums, mx)]
        Gcd.sort()
        ans = 0
        l, r= 0, n- 1
        while l< r:
            ans += gcd(Gcd[l], Gcd[r])
            l+= 1
            r-= 1
        return ans