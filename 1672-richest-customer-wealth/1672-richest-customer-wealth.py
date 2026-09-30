class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max = float('-inf')
        for r in accounts:
            sum = 0
            for c in r:
                sum += c
            if sum > max:
                max = sum
        return max