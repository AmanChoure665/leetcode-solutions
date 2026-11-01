class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        # s = s.split(" ")
        # return " ".join(s[:k])  # space o(n)

        for i in range(len(s)):
            if s[i] == " ":
                k -= 1
                if k == 0:
                    return s[:i]

        return s     # space complexity o(n)