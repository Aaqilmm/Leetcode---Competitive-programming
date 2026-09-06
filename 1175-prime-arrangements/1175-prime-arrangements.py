class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        mod = 10 ** 9 + 7
        is_prime = [True] * (n+1)
        is_prime[0] = False
        is_prime[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
        p = 0
        for i in range(1, n +1):
            if is_prime[i]:
                p += 1
        def fact(num):
            answer = 1
            for i in range(2, num+1):
                answer = (answer * i) % mod
            return answer
        final = fact(p) * fact(n-p)
        return final % mod

        