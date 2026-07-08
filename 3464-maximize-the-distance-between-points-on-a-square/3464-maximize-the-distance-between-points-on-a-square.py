class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        A = []
        for x, y in points:
            if y == 0:
                A.append(x)
            elif x == side:
                A.append(side + y)
            elif y == side:
                A.append(3 * side - x)
            else:
                A.append(4 * side - y)
        A.sort()
        n = len(A)
        B = A + [p + 4 * side for p in A]
        def isValid(d: int) -> bool:
            nxt = [2 * n] * (2 * n + 1)
            j = 0
            for i in range(2 * n):
                while j < 2 * n and B[j] - B[i] < d:
                    j += 1
                nxt[i] = j
            limit = 4 * side - d            
            for i in range(n):
                if i < n - 1 and nxt[i] == nxt[i + 1]:
                    continue
                curr = i
                for _ in range(k - 1):
                    curr = nxt[curr]
                if curr < 2 * n and B[curr] - B[i] <= limit:
                    return True
            return False
        low = 1
        high = side
        ans = 1
        
        while low <= high:
            mid = (low + high) // 2
            if isValid(mid):
                ans = mid
                low = mid + 1   
            else:
                high = mid - 1    
        return ans