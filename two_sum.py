class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ## Rather than broute forcing through all pairs
        ## Use a dict to save seen numbers
        ## Since the dict is implemented with hash table
        ## It optimised the search time of "target - nums[i]"
        tb = {}
        for i, num in enumerate(nums):
            if target - num in tb:
                return [tb[target-num], i]
            tb[num] = i
        return []
