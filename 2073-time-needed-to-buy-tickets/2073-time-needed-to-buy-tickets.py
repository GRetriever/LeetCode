class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        answer = 0
        
        while True:
            for i in range(len(tickets)):
                if tickets[i] > 0:
                    tickets[i] -= 1
                    answer += 1

                if i == k:
                    if tickets[i] == 0:
                        return answer
                