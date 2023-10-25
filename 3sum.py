class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans, n, i = [], len(nums), 0
        nums = sorted(nums)
        while i < n:
            ## Select the first number
            target = -1 * nums[i]
            
            ## Search for the second and third number pair
            front, back = i+1, n-1
            while front < back:
                s = nums[front] + nums[back]
                if s < target:
                    front += 1
                elif s > target:
                    back -= 1
                else:
                    tri = [nums[i], nums[front], nums[back]]
                    ans.append(tri)
                    
                    ## Skip through the same numbers of the second and third number
                    while front<back and nums[front]==tri[1]:
                        front += 1
                    while front<back and nums[back]==tri[2]:
                        back -= 1

            ## Skip through the same numbers of the first number
            while i+1<n and nums[i+1]==nums[i]:
                i += 1
            i += 1
        return ans
