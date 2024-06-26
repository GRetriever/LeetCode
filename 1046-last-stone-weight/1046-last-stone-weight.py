class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            y = stones[-1]
            stones.pop()
            x = stones[-1]
            stones.pop()

            if x == y:
                continue
            else:
                stones.append(y-x)
        return stones[0] if stones else 0