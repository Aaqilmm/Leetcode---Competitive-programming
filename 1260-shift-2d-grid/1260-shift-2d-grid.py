class Solution:
    def shiftGrid(self, g: List[List[int]], k: int) -> List[List[int]]:
        r, c = len(g), len(g[0])
        t = r * c
        k %= t
        a = [[0] * c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                x = (i * c + j + k) % t
                a[x // c][x % c] = g[i][j]
        return a