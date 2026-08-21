class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        coins.sort()
        n = len(coins)
        def count(x: int) -> int:
            total = 0
            for mask in range(1, 1 << n):
                l = 1
                valid = True
                for i in range(n):
                    if mask & (1 << i):
                        l = l * coins[i] // math.gcd(l, coins[i])
                        if l > x:
                            valid = False
                            break
                if not valid:
                    continue
                if bin(mask).count("1") % 2 == 1:
                    total += x // l
                else:
                    total -= x // l
            return total
        left, right = coins[0], k * coins[0]
        while left < right:
            mid = (left + right) // 2
            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1
        return left