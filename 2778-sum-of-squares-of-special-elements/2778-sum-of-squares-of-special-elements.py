class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        sum_of_sq = 0
        for i in range(n):
            if n%(i+1) == 0:
                sum_of_sq += nums[i] * nums[i]
        return sum_of_sq