class Solution:
    def minimumPushes(self, word: str) -> int:
        charcount = [0] * 26
        for ch in word:
            charcount[ord(ch) - ord('a')] += 1
        charcount.sort(reverse=True)
        minpushcount = 0
        for i in range(26):
            minpushcount += charcount[i] * (i // 8 + 1)
        return minpushcount