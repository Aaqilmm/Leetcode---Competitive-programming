class Solution:
    def gcd(self,a,b):
        while b:
            a,b = b,a % b
        return a
    def findGCD(self, nums: List[int]) -> int:
        mini = min(nums)
        maxi = max(nums)
        return self.gcd(mini,maxi)