class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n  = len(num1)-1
        m = len(num2)-1
        res = []
        reminder = 0
        while n >= 0 or m >= 0 or reminder:
            total = ((int(num1[n]) if n >= 0 else 0) +(int(num2[m]) if m >= 0 else 0) +reminder)
            res.append(str(total % 10))
            reminder = total // 10
            n -= 1
            m -= 1
        return "".join(reversed(res))