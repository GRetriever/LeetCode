class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        answer = 0
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                if nums[i] == nums[j] and i < j:
                    answer += 1
        return answer