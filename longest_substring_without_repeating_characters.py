class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        prev = collections.defaultdict(lambda: -1)
        ans, save = 0, -1
        for i, c in enumerate(s):
            ans = max(ans, i-max(prev[c], save))
            save = max(save, prev[c])
            prev[c] = i
        return ans
