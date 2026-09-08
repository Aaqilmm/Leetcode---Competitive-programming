class Solution:
    def countCommas(self, n: int) -> int:
        if len(str(n)) < 4:
            return 0
        else:
            s = str(n)
            m = len(s)
            s1 = "1"
            k = m-1
            l = k%3
            k=k-l
            for i in range(k):
                s1 = s1+"0"
            i1 = int(s1)
            d = n-i1
            return d+1