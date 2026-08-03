class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left, right +1, 1):
            s = str(i)
            for j in range(0, len(s), 1):
                flag = 1
                if int(s[j]) == 0:
                    break
                else:
                    if i%int(s[j]) == 0:
                        flag = 0
                    else:
                        flag = 1
                        break
            if flag == 0:
                    ans.append(i)
        return ans