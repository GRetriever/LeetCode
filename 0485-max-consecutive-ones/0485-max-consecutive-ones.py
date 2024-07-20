class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        answer = 0
        for i in nums:
            if i == 1:
                cnt += 1
                answer = max(answer,cnt)
            else:
                cnt = 0
        return answer