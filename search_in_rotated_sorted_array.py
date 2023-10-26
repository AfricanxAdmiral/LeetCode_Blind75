class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ## First Search for the point where nums[i] > nums[i+1] (O(logN))
        l, r = 0, len(nums)-1
        mid = (l+r)//2
        while l < r:
            if nums[mid] > nums[-1]: l = mid + 1
            else: r = mid
            mid = (l+r)//2
        
        ## Rotate the array back
        nums = nums[mid:] + nums[:mid]
        
        ## Then the ordinary binary search (O(logN))
        idx = bisect.bisect_left(nums, target)
        
        return -1 if (idx==len(nums) or nums[idx]!=target) else (idx+mid)%len(nums)
