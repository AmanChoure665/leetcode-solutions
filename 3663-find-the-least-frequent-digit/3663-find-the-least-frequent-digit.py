class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        temp = str(n)
        freq = {}
        for ch in temp:
            freq[ch] = freq.get(ch, 0) + 1
        
        min_freq = min(freq.values())
        
        res = float('inf')
        for digit, count in freq.items():
            if count == min_freq:
                res = min(res, int(digit))
        
        return res