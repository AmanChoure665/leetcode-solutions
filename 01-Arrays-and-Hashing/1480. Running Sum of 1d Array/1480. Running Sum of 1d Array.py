1class Solution:
2    def runningSum(self, nums: list[int]) -> list[int]:
3        for i in range(1,len(nums)):
4            nums[i] = nums[i-1] + nums[i]
5
6        return nums