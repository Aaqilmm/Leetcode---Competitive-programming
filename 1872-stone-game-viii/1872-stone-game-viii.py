class Solution:
    def stoneGameVIII(self, stones):
        n = len(stones)
        prefix = stones[:]
        for i in range(1, n):
            prefix[i] += prefix[i - 1]
        best = prefix[n - 1]
        for i in range(n - 2, 0, -1):
            best = max(best, prefix[i] - best)
        return best