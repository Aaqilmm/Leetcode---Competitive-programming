class Solution:
    def arrayRankTransform(self, arr):
        if not arr:
            return []
        dup = sorted(arr)
        np = {dup[0]: 1}
        for i in range(1, len(dup)):
            if dup[i] > dup[i - 1]:
                np[dup[i]] = np[dup[i - 1]] + 1
            else:
                np[dup[i]] = np[dup[i - 1]]
        return [np[x] for x in arr]