class Solution:
    def checkDivisibility(self, n: int) -> bool:
        a = str(n)
        summ = 0
        product = 1
        for i in a:
            summ = summ + int(i)
            product = product * int(i)
        tot = product + summ
        if n%tot == 0:
            return True
        return False