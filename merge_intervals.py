class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        prev_s, prev_e = -1, -1
        for s, e in sorted(intervals):
            if s > prev_e:
                ## start new interval if previous interval ends first
                ans.append([prev_s, prev_e])
                prev_s, prev_e = s, e
            else:
                prev_e = max(prev_e, e)
        ans.append([prev_s, prev_e])

        return ans[1:]
