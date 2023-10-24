class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tb = {}
        for i, num in enumerate(nums):
            if target - num in tb:
                return [tb[target-num], i]
            tb[num] = i
        return []
