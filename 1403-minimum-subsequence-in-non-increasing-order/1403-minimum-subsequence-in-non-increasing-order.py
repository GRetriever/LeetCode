class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums = sorted(nums,reverse=True)
        for i in range(len(nums)):
            if sum(nums[:i+1]) > sum(nums[i+1:]):
                return nums[:i+1]