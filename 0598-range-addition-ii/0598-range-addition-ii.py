class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m * n
        minX = min(op[0] for op in ops)
        minY = min(op[1] for op in ops)
        return minX * minY