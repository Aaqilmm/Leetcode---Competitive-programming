class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        ones = s.count('1')
        s = '1' + s + '1'
        n = len(s)
        i = 0
        ans = ones
        while i < n and s[i] == '1':
            i += 1
        a = 0
        while i < n and s[i] == '0':
            a += 1
            i += 1
        while i < n:
            b = 0
            while i < n and s[i] == '1':
                b += 1
                i += 1
            if b == 0:
                break
            c = 0
            while i < n and s[i] == '0':
                c += 1
                i += 1
            if c == 0:
                break
            ans = max(ans, ones + a + c)
            a = c
        return ans