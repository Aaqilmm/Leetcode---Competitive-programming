class Solution:
    def maxProduct(self, n: int) -> int:
        m = 0
        while n:
            m += 1 << ((n % 10) << 2)
            n //= 10
        u = (m.bit_length() - 1) >> 2
        return u * (((m - (1 << (u << 2))).bit_length() - 1) >> 2)