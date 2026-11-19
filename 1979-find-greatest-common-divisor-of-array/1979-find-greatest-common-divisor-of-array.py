class Solution:
    def findGCD(self, nums: list[int]) -> int:
        maxi = max(nums)
        mini = min(nums)
        com = 0

        for i in range(1,mini+1):
            if maxi % i == 0 and mini % i == 0:
                com = i
            else:
                continue
        return com