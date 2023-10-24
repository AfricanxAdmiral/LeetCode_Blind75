class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ## If the length of set does not equal to the original length
        ## There exists duplicate digits
        return len(set(nums))!=len(nums)
