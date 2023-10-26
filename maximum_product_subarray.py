class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ## Max product till the previous is the thing tha only matters
        ans = imax = imin = nums[0]
        for num in nums[1:]:
            ## if num < 0, the min product became the max, vice versa
            if num < 0:
                imax, imin = imin, imax
            imax = max(num, imax*num)
            imin = min(num, imin*num)
            ans = max(ans, imax)
        return ans
