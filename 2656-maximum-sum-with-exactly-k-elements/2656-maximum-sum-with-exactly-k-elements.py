class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        maxi = max(nums)
        # total = 0
        # while k > 0:
        #     total += maxi
        #     maxi += 1
        #     k -= 1
        # return total

        return k * (2 * maxi + k - 1) // 2