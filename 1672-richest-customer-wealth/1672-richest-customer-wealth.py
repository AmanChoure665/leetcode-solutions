class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        ans = []
        for i in accounts:
            n = 0
            for j in i:
                n = n + j
            ans.append(n)
        return max(ans)