class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0
        p = 1000
        commas = 1
        ans = 0
        while p <= n:
            end = min(n, p * 1000 - 1)
            ans += (end - p + 1) * commas
            p *= 1000
            commas += 1
        return ans