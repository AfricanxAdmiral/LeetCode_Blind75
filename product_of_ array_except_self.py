class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1 for _ in range(n)]

        ## First compute the product of the left side of each position
        cur = 1
        for i in range(n):
            ans[i] *= cur
            cur *= nums[i]

        ## Then compute the product of the right side
        ## and multiple with previous computed left product
        cur = 1
        for i in range(n-1, -1, -1):
            ans[i] *= cur
            cur *= nums[i]

        return ans
