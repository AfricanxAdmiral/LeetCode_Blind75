class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxf = ans = 0
        cnt = collections.Counter()
        for i in range(len(s)):
            cnt[s[i]] += 1
            maxf = max(maxf, cnt[s[i]])
            if ans - maxf < k:
                ans += 1
            else:
                cnt[s[i-ans]] -= 1
        return ans
