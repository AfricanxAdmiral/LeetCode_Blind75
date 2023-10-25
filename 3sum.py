class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans, n, i = [], len(nums), 0
        nums = sorted(nums)
        while i < n:
            # print(f"i: {i}")
            target = -1 * nums[i]
            front = i + 1
            back = n-1
            while front < back:
                s = nums[front] + nums[back]
                if s < target:
                    front += 1
                elif s > target:
                    back -= 1
                else:
                    tri = [nums[i], nums[front], nums[back]]
                    ans.append(tri)
                    while front<back and nums[front]==tri[1]:
                        front += 1
                    while front<back and nums[back]==tri[2]:
                        back -= 1
            
            while i+1<n and nums[i+1]==nums[i]:
                i += 1
            i += 1
        return ans
