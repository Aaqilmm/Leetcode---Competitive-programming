class Solution:
    s = ["Bob", "Tie", "Alice"]
    def stoneGameIII(self, A: List[int]) -> str:
        n = len(A)
        @cache
        def maxdiff(i: int) -> int:
            if i == n: return 0
            a = b = c = -5e7
            if i < n:
                a = A[i] - maxdiff(i + 1)
            if i + 1 < n:
                b = A[i] + A[i + 1] - maxdiff(i + 2)
            if i + 2 < n:
                c = A[i] + A[i + 1] + A[i + 2] - maxdiff(i + 3)
            return max(a, b, c)
        d = maxdiff(0)
        return self.s[(d > 0) - (d < 0) + 1]